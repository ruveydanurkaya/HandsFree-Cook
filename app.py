import cv2
import pandas as pd
import ast
import mediapipe as mp

# --- TÜRKÇE KARAKTER DÜZELTİCİ ---
def turkce_karakter_temizle(metin):
    tr_map = {'ç': 'c', 'ğ': 'g', 'ı': 'i', 'ö': 'o', 'ş': 's', 'ü': 'u',
              'Ç': 'C', 'Ğ': 'G', 'İ': 'I', 'Ö': 'O', 'Ş': 'S', 'Ü': 'U'}
    for key, value in tr_map.items():
        metin = metin.replace(key, value)
    return metin

# --- 1. VERİ SETİNİ YÜKLEME ---
df = pd.read_csv("benim_tariflerim.csv")

secili_tarif_index = 0
tarif_adi = str(df.iloc[secili_tarif_index]['tarif_adi']).upper()
tarif_adimlari = ast.literal_eval(df.iloc[secili_tarif_index]['adimlar']) 

guncel_adim = 0

# --- 2. MEDIAPIPE (El Takibi) AYARLARI ---
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# --- 3. KAMERA VE SANAL BÖLGE DEĞİŞKENLERİ ---
cap = cv2.VideoCapture(0)

# "Geri çekme (Return Stroke)" hatasını önlemek için kilit sistemi:
# Kullanıcı bir butona dokunduktan sonra tekrar tetiklemek için elini ekranın ortasına getirmek zorundadır.
el_merkezde = True 

print("Sistem Başladı! 'İLERİ' veya 'GERİ' kutularına dokunun.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
        
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape
    
    # Ekranın genişliğine göre sanal bölgelerin sınırları hesaplanıyor
    sol_sinir = int(w * 0.25)  # Ekranın sol %25'i
    sag_sinir = int(w * 0.75)  # Ekranın sağ %25'i
    
    # --- EKRANA SANAL BÖLGELERİ ÇİZELİM ---
    # Geri Butonu Çizgisi (Kırmızı)
    cv2.line(frame, (sol_sinir, 130), (sol_sinir, h), (0, 0, 255), 2)
    cv2.putText(frame, "<- GERI", (10, int(h/2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    # İleri Butonu Çizgisi (Yeşil)
    cv2.line(frame, (sag_sinir, 130), (sag_sinir, h), (0, 255, 0), 2)
    cv2.putText(frame, "ILERI ->", (sag_sinir + 10, int(h/2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    # --- JEST KONTROL MANTIĞI (Sanal Bölge) ---
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # İşaret parmağının piksel cinsinden X konumu
            isaret_x = int(hand_landmarks.landmark[8].x * w)
            
            # Eğer parmak SAĞ taraftaki İLERİ kutusuna girdiyse
            if isaret_x > sag_sinir:
                if el_merkezde: # Eğer el daha önce ortadaysa işlemi yap
                    if guncel_adim < len(tarif_adimlari) - 1:
                        guncel_adim += 1
                        print("👉 İleri Kutusuna Dokunuldu")
                    el_merkezde = False # Eli merkezden çıktı olarak işaretle (Kilitle)
                    
            # Eğer parmak SOL taraftaki GERİ kutusuna girdiyse
            elif isaret_x < sol_sinir:
                if el_merkezde:
                    if guncel_adim > 0:
                        guncel_adim -= 1
                        print("👈 Geri Kutusuna Dokunuldu")
                    el_merkezde = False # Eli merkezden çıktı olarak işaretle (Kilitle)
                    
            # Eğer parmak ORTA BÖLÜMDEYSE (Güvenli Alan)
            else:
                el_merkezde = True # Kilidi aç, kullanıcı yeniden butonlara basabilir

    # --- ARAYÜZ (EKRANA YAZDIRMA) ---
    adim_metni = turkce_karakter_temizle(tarif_adimlari[guncel_adim])
    gosterilecek_metin = adim_metni[:70] + "..." if len(adim_metni) > 70 else adim_metni
    
    # Üst Bilgi Kutusu
    cv2.rectangle(frame, (10, 10), (w-10, 120), (0, 0, 0), -1)
    cv2.putText(frame, f"Tarif: {tarif_adi}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
    cv2.putText(frame, f"Adim {guncel_adim + 1}/{len(tarif_adimlari)}:", (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
    cv2.putText(frame, gosterilecek_metin, (20, 105), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    
    cv2.imshow("Temassiz Tarif Asistani", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()