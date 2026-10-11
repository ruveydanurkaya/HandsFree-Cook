import pandas as pd
import json

# 10 tariflik zengin veri setimiz ve hazırlık süreleri (dakika)
veri = [
    {
        "tarif_adi": "Karnıyarık",
        "sure": 45,
        "adimlar": json.dumps([
            "Patlıcanları alacalı soyup yağda hafifçe kızartın.",
            "Soğan, biber ve kıymayı tavada kavurarak iç harcı hazırlayın.",
            "Kızaran patlıcanların ortasını yarıp iç harcı doldurun.",
            "Salçalı su ekleyip önceden ısıtılmış fırında 25 dakika pişirin.",
            "Sıcak servis yapın, afiyet olsun."
        ])
    },
    {
        "tarif_adi": "Mercimek Çorbası",
        "sure": 30,
        "adimlar": json.dumps([
            "Soğan, havuç ve patatesi doğrayıp tencerede yağ ile kavurun.",
            "Yıkanmış kırmızı mercimekleri ekleyip 1-2 dakika daha kavurun.",
            "Üzerine sıcak su ve tuz ekleyip sebzeler yumuşayana kadar kaynatın.",
            "Tüm malzemeleri blenderdan geçirip pürüzsüz hale getirin.",
            "Üzerine tereyağında kızdırılmış nane dökerek servis yapın."
        ])
    },
    {
        "tarif_adi": "Menemen",
        "sure": 15,
        "adimlar": json.dumps([
            "İnce doğranmış sivri biberleri sıvı yağda hafifçe kavurun.",
            "Kabukları soyulmuş ve küp küp doğranmış domatesleri tavaya ekleyin.",
            "Domatesler suyunu çekip yumuşayana kadar kısık ateşte pişirin.",
            "Yumurtaları kırıp tuz ekleyin ve hafifçe karıştırın.",
            "Yumurtalar pişene kadar bekleyip ocaktan alın."
        ])
    },
    {
        "tarif_adi": "Kısır",
        "sure": 20,
        "adimlar": json.dumps([
            "İnce bulguru geniş bir kaba alıp üzerini geçecek kadar sıcak su ekleyin.",
            "Bulgurlar şiene kadar üzerini kapatıp 10 dakika bekletin.",
            "Domates ve biber salçası ekleyip bulgura iyice yedirerek yoğurun.",
            "İnce kıyılmış taze soğan, maydanoz ve kıvırcığı ekleyin.",
            "Limon suyu, nar ekşisi ve zeytinyağı ilave edip karıştırın."
        ])
    },
    {
        "tarif_adi": "Kremalı Mantarlı Tagliatelle",
        "sure": 25,
        "adimlar": json.dumps([
            "Makarnayı tuzlu kaynar suda 10 dakika haşlayıp suyunu süzün.",
            "Ayrı bir tavada zeytinyağını ısıtıp dilimlenmiş mantarları ekleyin.",
            "Mantarlar suyunu çekene kadar yaklaşık 5 dakika kavurun.",
            "Sosu krema ve taze fesleğen ile bağlayıp kısık ateşte 2 dakika ısıtın.",
            "Haşlanan makarnaları sosa ilave edip iyice harmanlayın."
        ])
    },
    {
        "tarif_adi": "Fırın Somon",
        "sure": 35,
        "adimlar": json.dumps([
            "Somon filetolarını yıkayıp kağıt havlu ile kurulayın.",
            "Zeytinyağı, limon suyu, tuz ve baharatları bir kasede karıştırın.",
            "Soslu karışımı somonların üzerine fırçayla homojen şekilde sürün.",
            "Fırın tepsisine yağlı kağıt serip somonları ve taze biberiyeleri dizin.",
            "Önceden ısıtılmış 200 derece fırında 20 dakika pişirin."
        ])
    },
    {
        "tarif_adi": "Avokadolu Poşe Yumurta",
        "sure": 15,
        "adimlar": json.dumps([
            "Olgun avokadoyu çatal ile ezerek limon suyu ve tuzla püreyi hazırlayın.",
            "Tencerede kaynayan suya bir kaşık sirke ekleyip girdap oluşturun.",
            "Yumurtayı girdabın ortasına kırıp 3 dakika haşlayın.",
            "Kızarmış ekmek dilimlerine avokado püresini sürün.",
            "Üzerine poşe yumurtayı yerleştirip servis yapın."
        ])
    },
    {
        "tarif_adi": "Akdeniz Salatası",
        "sure": 15,
        "adimlar": json.dumps([
            "Domates, salatalık ve biberleri küp şeklinde doğrayın.",
            "Geniş bir kaseye aldığınız sebzelere siyah zeytin ekleyin.",
            "Zeytinyağı, limon suyu ve tuzu bir kasede çırpıp salataya gezdirin.",
            "Üzerine küp doğranmış beyaz peynir ekleyip hafifçe karıştırın."
        ])
    },
    {
        "tarif_adi": "Ev Yapımı Lahmacun",
        "sure": 50,
        "adimlar": json.dumps([
            "Un, su ve mayayı yoğurarak yumuşak bir hamur elde edin.",
            "Kıyma, soğan, domates, biber ve baharatları robottan geçirip harç hazırlayın.",
            "Mayalanan hamurdan bezeler yapıp merdaneyle incece açın.",
            "Hazırladığınız iç harcı hamurun üzerine ince bir tabaka halinde yayın.",
            "Önceden ısıtılmış yüksek dereceli fırında altı kızarana kadar pişirin."
        ])
    },
    {
        "tarif_adi": "Fırında Sütlaç",
        "sure": 45,
        "adimlar": json.dumps([
            "Pirinci yıkayıp suda yumuşayana kadar haşlayın.",
            "Süt ve şekeri tencerede kaynatıp haşlanmış pirinçleri ekleyin.",
            "Nişastayı az suyla açıp tencereye yavaşça dökerek kıvam verin.",
            "Vanilya ekleyip karıştırın ve ısıya dayanıklı kaplara paylaştırın.",
            "Fırın tepsisine su koyup kapları dizin ve üzerleri kızarana kadar fırınlayın."
        ])
    }
]

# DataFrame'e dönüştürüp CSV olarak kaydediyoruz
df = pd.DataFrame(veri)
df.to_csv('benim_tariflerim.csv', index=False, encoding='utf-8')

print("Harika! 'benim_tariflerim.csv' hazırlama süreleriyle birlikte güncellendi.")