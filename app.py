from flask import Flask, render_template, Response, jsonify
import cv2
import pandas as pd
import ast
import mediapipe as mp

app = Flask(__name__)

# Veri setini yükle
try:
    df = pd.read_csv("recipes.csv")
except:
    print("HATA: 'recipes.csv' bulunamadı!")
    exit()

secili_tarif_index = 0
guncel_adim = 0
el_merkezde = True

# MediaPipe ayarları
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# 1. YENİ ANA SAYFA (Katalog Sayfası)
@app.route('/')
def index():
    # Tariflerin tümünü sözlük olarak ana sayfaya gönder
    tarifler_listesi = df.to_dict('records')
    return render_template('index.html', tarifler=tarifler_listesi)

# 2. KAMERA MODU SAYFASI
@app.route('/kamera/<int:tarif_id>')
def kamera(tarif_id):
    global secili_tarif_index, guncel_adim
    secili_tarif_index = tarif_id
    guncel_adim = 0
    tarifler_listesi = df.to_dict('records')
    return render_template('kamera.html', tarifler=tarifler_listesi)

# API ve Kamera Akışı Route'ları (Aynı kalıyor)
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
    
    # Yeni eklenen malzemeler satırı:
    malzemeler = ast.literal_eval(df.iloc[secili_tarif_index]['malzemeler'])
    
    return jsonify({
        'tarif_adi': tarif_adi,
        'sure': tarif_suresi,
        'guncel_adim': guncel_adim,
        'toplam_adim': len(tarif_adimlari),
        'adim_metni': tarif_adimlari[guncel_adim],
        'malzemeler': malzemeler  # HTML'e gönderiyoruz
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
        
        ileri_parliyor = False
        geri_parliyor = False
        
        # El Jest Kontrolü (Apple Tarzı Yumuşak İmleç)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                isaret_x = int(hand_landmarks.landmark[8].x * w)
                isaret_y = int(hand_landmarks.landmark[8].y * h)
                
                cv2.circle(frame, (isaret_x, isaret_y), 4, (255, 255, 255), -1)
                overlay_circle = frame.copy()
                cv2.circle(overlay_circle, (isaret_x, isaret_y), 8, (255, 255, 255), -1)
                cv2.addWeighted(overlay_circle, 0.4, frame, 0.6, 0, dst=frame)
                
                if isaret_x > sag_sinir:
                    ileri_parliyor = True
                    if el_merkezde and guncel_adim < len(tarif_adimlari) - 1:
                        guncel_adim += 1
                        el_merkezde = False
                elif isaret_x < sol_sinir:
                    geri_parliyor = True
                    if el_merkezde and guncel_adim > 0:
                        guncel_adim -= 1
                        el_merkezde = False
                else:
                    el_merkezde = True

        # Yumuşak Kenar Parlamaları
        overlay = frame.copy()
        if geri_parliyor:
            for i in range(40):
                alpha = (40 - i) / 40.0 * 0.35
                cv2.rectangle(overlay, (i, 0), (i+1, h), (0, 0, 255), -1)
                cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, dst=frame)
                
        if ileri_parliyor:
            for i in range(40):
                alpha = (40 - i) / 40.0 * 0.35
                cv2.rectangle(overlay, (w - i - 1, 0), (w - i, h), (0, 255, 0), -1)
                cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, dst=frame)

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