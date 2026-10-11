from flask import Flask, render_template, Response, jsonify
import cv2
import pandas as pd
import ast
import mediapipe as mp

app = Flask(__name__)

# Veri setini yükle
try:
    df = pd.read_csv("benim_tariflerim.csv")
except:
    print("HATA: 'benim_tariflerim.csv' bulunamadı!")
    exit()

secili_tarif_index = 0
guncel_adim = 0
el_merkezde = True

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

def turkce_karakter_temizle(metin):
    tr_map = {'ç':'c','ğ':'g','ı':'i','ö':'o','ş':'s','ü':'u','Ç':'C','Ğ':'G','İ':'I','Ö':'O','Ş':'S','Ü':'U'}
    for key, value in tr_map.items(): metin = metin.replace(key, value)
    return metin

@app.route('/')
def index():
    # Sadece isimleri değil, her iki sütunu da sözlük olarak gönderiyoruz
    tarifler_listesi = df[['tarif_adi', 'sure']].to_dict('records')
    return render_template('index.html', tarifler=tarifler_listesi)

@app.route('/set_recipe/<int:index>')
def set_recipe(index):
    global secili_tarif_index, guncel_adim
    secili_tarif_index = index
    guncel_adim = 0
    return get_status()

@app.route('/get_status')
def get_status():
    tarif_adi = str(df.iloc[secili_tarif_index]['tarif_adi'])
    tarif_suresi = int(df.iloc[secili_tarif_index]['sure'])
    tarif_adimlari = ast.literal_eval(df.iloc[secili_tarif_index]['adimlar'])
    return jsonify({
        'tarif_adi': tarif_adi,
        'sure': tarif_suresi,
        'guncel_adim': guncel_adim,
        'toplam_adim': len(tarif_adimlari),
        'adim_metni': tarif_adimlari[guncel_adim]
    })

def generate_frames():
    global secili_tarif_index, guncel_adim, el_merkezde
    cap = cv2.VideoCapture(0)
    
    while True:
        success, frame = cap.read()
        if not success:
            break
            
        frame = cv2.flip(frame, 1)
        h, w, c = frame.shape
        sol_sinir, sag_sinir = int(w * 0.20), int(w * 0.80)
        
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)
        
        tarif_adimlari = ast.literal_eval(df.iloc[secili_tarif_index]['adimlar'])
        
        # El Jest Kontrolü
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                isaret_x = int(hand_landmarks.landmark[8].x * w)
                isaret_y = int(hand_landmarks.landmark[8].y * h)
                
                # Parmak ucuna estetik imleç
                cv2.circle(frame, (isaret_x, isaret_y), 16, (0, 230, 118), 2)
                cv2.circle(frame, (isaret_x, isaret_y), 4, (255, 255, 255), -1)
                
                if isaret_x > sag_sinir:
                    cv2.rectangle(frame, (sag_sinir, 0), (w, h), (0, 255, 0), 4)
                    if el_merkezde and guncel_adim < len(tarif_adimlari) - 1:
                        guncel_adim += 1
                        el_merkezde = False
                elif isaret_x < sol_sinir:
                    cv2.rectangle(frame, (0, 0), (sol_sinir, h), (0, 0, 255), 4)
                    if el_merkezde and guncel_adim > 0:
                        guncel_adim -= 1
                        el_merkezde = False
                else:
                    el_merkezde = True

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    print("🚀 HandsFree-Cook Web Sunucusu Çalışıyor: http://127.0.0.1:5000")
    app.run(debug=True, port=5000)