import pandas as pd
import json

# Kendi özel veri setimizi sözlük (dictionary) yapısında oluşturuyoruz.
# Adımları tam senin arayüzünün (swipe) seveceği gibi kısa ve net maddelere böldüm.
veri = [
    {
        "tarif_adi": "Karniyarik",
        "adimlar": json.dumps([
            "Patlicanlari alacali soyup yagda hafifce kizartin.",
            "Sogan, biber ve kiymayi tavada kavurarak ic harci hazirlayin.",
            "Kizaran patlicanlarin ortasini yarip ic harci doldurun.",
            "Salcali su ekleyip onceden isitilmis firinda 25 dakika pisirin.",
            "Sicak servis yapin, afiyet olsun."
        ])
    },
    {
        "tarif_adi": "Mercimek Corbasi",
        "adimlar": json.dumps([
            "Sogan, havuc ve patatesi dograyip tencerede yag ile kavurun.",
            "Yikanmis kirmizi mercimekleri ekleyip 1-2 dakika daha kavurun.",
            "Uzerine sicak su ve tuz ekleyip sebzeler yumusayana kadar kaynatin.",
            "Tum malzemeleri blenderdan gecirip puruzsuz hale getirin.",
            "Uzerine tereyaginda kizdirilmis nane dokerek servis yapin."
        ])
    },
    {
        "tarif_adi": "Menemen",
        "adimlar": json.dumps([
            "Ince dogranmis sivri biberleri sivi yagda hafifce kavurun.",
            "Kabuklari soyulmus ve kup kup dogranmis domatesleri tavaya ekleyin.",
            "Domatesler suyunu cekip yumusayana kadar kisik ateste pisirin.",
            "Yumurtalari kirip tuz ekleyin ve hafifce karistirin.",
            "Yumurtalar pisine kadar bekleyip ocaktan alin."
        ])
    },
    {
        "tarif_adi": "Kısır",
        "adimlar": json.dumps([
            "Ince bulguru genis bir kaba alip uzerini gececek kadar sicak su ekleyin.",
            "Bulgurlar sisene kadar uzerini kapatip 10 dakika bekletin.",
            "Domates ve biber salcasi ekleyip bulgura iyice yedirerek yogurun.",
            "Ince kiyilmis taze sogan, maydanoz ve kivircigi ekleyin.",
            "Limon suyu, nar eksisi ve zeytinyagi ilave edip karistirin."
        ])
    }
]

# Veriyi Pandas DataFrame'e çevirip CSV olarak kaydediyoruz
df = pd.DataFrame(veri)
df.to_csv('benim_tariflerim.csv', index=False, encoding='utf-8')

print("Harika! 'benim_tariflerim.csv' adli ozel veri setin basariyla olusturuldu.")