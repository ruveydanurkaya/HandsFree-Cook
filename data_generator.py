import pandas as pd
import json

base_url = "https://yemekyarismasi.com"

veri = [
    # --- BALIK TARİFLERİ ---
    {
        "tarif_adi": "Fırında Zeytinyağlı Sardalya",
        "sure": 45,
        "kategori": "Balık Tarifleri",
        "gorsel_url": f"{base_url}/resim/firinda-zeytinyagli-sardalya-tarifi.webp",
        "ozet": "Taze otlar, zeytinyağı ve limonla harmanlanmış, fırında nar gibi kızaran hafif ve sağlıklı bir balık ziyafeti.",
        "malzemeler": json.dumps(["500g temizlenmiş sardalya", "2 adet kırmızı soğan", "15-20 adet çeri domates", "Yarım çay bardağı zeytinyağı", "1 adet limon", "Tuz, karabiber"]),
        "adimlar": json.dumps([
            "Sardalyaları temizleyip yıkayın ve suyunu süzün.",
            "Kırmızı soğanları halka halka doğrayıp tepsinin tabanına dizin.",
            "Üzerine sardalyaları yerleştirip çeri domates ve sarımsakları ekleyin.",
            "Zeytinyağı, limon suyu, tuz ve karabiberi karıştırıp balıkların üzerinde gezdirin.",
            "Önceden ısıtılmış 200 derece fırında 25-30 dakika pişirin."
        ])
    },
    {
        "tarif_adi": "Tavada Lüfer Fileto",
        "sure": 25,
        "kategori": "Balık Tarifleri",
        "gorsel_url": f"{base_url}/resim/tavada-lufer-fileto-tarifi.webp",
        "ozet": "Zeytinyağı ve taze baharatlar eşliğinde döküm tavada mühürlenmiş nefis lüfer fileto.",
        "malzemeler": json.dumps(["2 adet lüfer fileto", "1 su bardağı çeri domates", "3 yemek kaşığı zeytinyağı", "2 diş sarımsak", "Taze kekik ve maydanoz", "Tuz, karabiber"]),
        "adimlar": json.dumps([
            "Lüfer filetolarını yıkayıp kağıt havlu ile kurulayın ve tuzlayın.",
            "Tavada zeytinyağını ısıtıp ince dilimlenmiş sarımsakları ekleyin.",
            "Balıkları derili kısmı alta gelecek şekilde tavaya yerleştirin.",
            "Yarıya kesilmiş çeri domatesleri ve taze kekikleri kenarlarına ekleyin.",
            "Her iki yüzünü de kısa süre pişirip sıcak servis yapın."
        ])
    },

    {
            "tarif_adi": "Fırında Sebzeli Kalkan Balığı",
            "sure": 30,
            "kategori": "Balık Tarifleri",
            "gorsel_url": f"{base_url}/resim/firinda-sebzeli-kalkan-baligi-tarifi.webp",
            "ozet": "Sanatsal sunumu ve özel sosuyla fırında nar gibi kızaran nefis sebzeli kalkan balığı.",
            "malzemeler": json.dumps(["1 adet kalkan balığı", "Zeytinyağı", "Sarımsak", "Taze kekik", "Limon suyu"]),
            "adimlar": json.dumps([
                "Kalkan balığını temizleyip fırın tepsisine yerleştirin.",
                "Zeytinyağı, sarımsak ve limon suyunu karıştırarak sos hazırlayın.",
                "Sosu balığın her yerine sürün ve kekik ekleyin.",
                "200 derece fıronda 30 dakika pişirin."
            ])
        },

    # --- HAMUR İŞİ ---
    {
        "tarif_adi": "Evde Kaşarlı Sucuklu Pide",
        "sure": 75,
        "kategori": "Hamur İşi",
        "gorsel_url": f"{base_url}/resim/evde-pide-tarifi.webp",
        "ozet": "Dışı çıtır, içi yumuşacık hamuruyla fırından yeni çıkmış bol malzemeli nefis ev yapımı pide.",
        "malzemeler": json.dumps(["500g un", "1 bardak ılık su", "Yarım bardak ılık süt", "1 paket kuru maya", "200g kaşar peyniri", "150g sucuk"]),
        "adimlar": json.dumps([
            "Un, ılık su, süt, maya, şeker ve tuzu karıştırıp yumuşak bir hamur yoğurun.",
            "Hamurun üzerini kapatıp 45 dakika mayalanmaya bırakın.",
            "Mayalanan hamurdan bezeler alıp uzunlamasına oval şekilde açın.",
            "Ortasına rendelenmiş kaşar ve sucuk dilimlerini yerleştirip kenarlarını kıvırın.",
            "Kenarlarına yumurta sarısı sürüp 200 derece fırında kızarana kadar pişirin."
        ])
    },
    {
        "tarif_adi": "Çıtır Sokak Simidi",
        "sure": 60,
        "kategori": "Hamur İşi",
        "gorsel_url": f"{base_url}/resim/simit-tarifi.webp",
        "ozet": "Evde kolayca yapabileceğiniz, dışı bol susamlı, pekmezli ve çıtır çıtır gerçek sokak simidi.",
        "malzemeler": json.dumps(["4 su bardağı un", "1.5 su bardağı ılık su", "1 paket maya", "Yarım çay bardağı sıvı yağ", "1 çay bardağı pekmez", "Bol kavrulmuş susam"]),
        "adimlar": json.dumps([
            "Un, ılık su, maya, şeker, tuz ve sıvı yağı karıştırarak ele yapışmayan bir hamur yoğurun.",
            "Hamuru 45 dakika mayalandırın.",
            "Pekmez ve suyu geniş bir kapta karıştırın, susamları tavada hafifçe kavurun.",
            "Hamurdan bezeler alıp şeritler halinde uzatın, ikili burgu yapıp halka şekli verin.",
            "Simitleri önce pekmezli suya, sonra susama bulayıp 200 derece fırında pişirin."
        ])
    },
    {
        "tarif_adi": "İtalyan Ekmeği Focaccia",
        "sure": 65,
        "kategori": "Hamur İşi",
        "gorsel_url": f"{base_url}/resim/italyan-ekmegi-focaccia-tarifi.webp",
        "ozet": "Zeytinyağı ve taze baharatların enfes kokusuyla taçlanmış, dışı çıtır içi yumuşacık İtalyan bahçe ekmeği.",
        "malzemeler": json.dumps(["500g un", "400ml ılık su", "1 paket kuru maya", "Yarım çay bardağı zeytinyağı", "Biberiye, taze kekik", "Kaya tuzu, zeytin, çeri domates"]),
        "adimlar": json.dumps([
            "Un, ılık su, maya, şeker, tuz ve zeytinyağı ile çok yumuşak bir hamur yoğurun.",
            "Hamuru yağlanmış fırın kabına alıp üzerini kapatarak 1 saat mayalandırın.",
            "Parmak uçlarınızı yağlayıp hamurun üzerine bastırarak çukurlar oluşturun.",
            "Üzerine zeytinyağı gezdirip biber, soğan veya zeytin ile süsleyin.",
            "200 derece fırında üzeri altın sarısı olana kadar pişirin."
        ])
    },

    # --- TAVUK TARİFLERİ ---
    {
        "tarif_adi": "Mantarlı Tavuk Jülyen",
        "sure": 25,
        "kategori": "Tavuk Tarifleri",
        "gorsel_url": f"{base_url}/resim/mantarli-tavuk-julyen-tarifi.webp",
        "ozet": "Krema ve mantarın muhteşem uyumuyla hazırlanan, damak çatlatan pratik ve doyurucu tavuk jülyen.",
        "malzemeler": json.dumps(["500g tavuk göğsü", "300g taze mantar", "1 kutu (200ml) krema", "1 adet kuru soğan", "2 diş sarımsak", "Sıvı yağ, tuz, kekik"]),
        "adimlar": json.dumps([
            "Tavuk göğsünü jülyen (uzun ince) şekilde doğrayın.",
            "Tavada sıvı yağı ısıtıp tavukları suyunu salıp çekene kadar soteleyin.",
            "Doğranmış soğan, sarımsak ve mantarları ekleyip kavurmaya devam edin.",
            "Mantarlar suyunu çekince kremayı, tuzu ve baharatları ilave edin.",
            "Kısık ateşte sos koyulaşana kadar 5 dakika daha pişirip sıcak servis yapın."
        ])
    },
    
    # --- BÖREK TARİFLERİ ---
    {
        "tarif_adi": "Kıymalı Gül Böreği",
        "sure": 30,
        "kategori": "Börek Tarifleri",
        "gorsel_url": f"{base_url}/resim/kiymali-gul-borek-tarifi.webp",
        "ozet": "Hazır yufkadan yapılan, dışı çıtır içi ise yumuşacık, porsiyonluk nefis kıymalı açık gül böreği.",
        "malzemeler": json.dumps(["3-4 adet taze yufka", "300g dana kıyma", "1 adet kuru soğan", "1 çay bardağı süt", "Yarım çay bardağı sıvı yağ", "Tuz, karabiber"]),
        "adimlar": json.dumps([
            "Kıymayı soğan ve sıvı yağ ile tavada kavurun, baharatlarını ekleyip soğutun.",
            "Yufkaları dörde bölerek üçgen parçalar elde edin.",
            "Süt, sıvı yağ ve maden suyu ile hazırladığınız sosu yufkalara sürün.",
            "Geniş kısma kıymalı harcı koyup rulo sarın ve kendi etrafında dolayarak gül şekli verin.",
            "Üzerine yumurta sarısı sürüp 180 derece fırında kızarana kadar pişirin."
        ])
    },
    {
        "tarif_adi": "Peynirli Banitsa Böreği",
        "sure": 40,
        "kategori": "Börek Tarifleri",
        "gorsel_url": f"{base_url}/resim/peynirli-banitsa-tarifi.webp",
        "ozet": "Yoğurtlu ve yumurtalı özel sosuyla kat kat kabaran, geleneksel peynirli Bulgaristan böreği.",
        "malzemeler": json.dumps(["500g yufka", "400g beyaz peynir", "4 adet yumurta", "250g yoğurt", "150g eritilmiş tereyağı"]),
        "adimlar": json.dumps([
            "Yumurta, yoğurt ve erimiş tereyağını bir kapta çırparak sos hazırlayın.",
            "Yufkayı tezgaha serip üzerine sostan ve ufalanmış peynirden yayın.",
            "Yufkayı rulo şeklinde sarıp kendi etrafında döndürerek tepsinin ortasına yerleştirin.",
            "Kalan yufkaları da aynı şekilde sarıp merkezin etrafına dolayın.",
            "Kalan sosu üzerine sürüp 190 derece fırında kızarana kadar pişirin."
        ])
    },

    # --- TATLI TARİFLERİ ---
    {
        "tarif_adi": "Şekerpare",
        "sure": 40,
        "kategori": "Tatlı Tarifleri",
        "gorsel_url": f"{base_url}/resim/sekerpare-tarifi.webp",
        "ozet": "Ağızda dağılan kıvamı ve tam ölçülü şerbetiyle çay saatlerinin vazgeçilmezi, pastane usulü şekerpare.",
        "malzemeler": json.dumps(["125g tereyağı", "Yarım su bardağı pudra şekeri", "2 adet yumurta", "1 su bardağı irmik", "2.5 su bardağı un", "Şerbet: 3 bardak şeker, 3 bardak su"]),
        "adimlar": json.dumps([
            "Su ve şekeri kaynatıp içine limon sıkarak şerbeti hazırlayın ve soğumaya bırakın.",
            "Oda sıcaklığındaki tereyağı, pudra şekeri ve yumurtayı karıştırın.",
            "İrmik, un, kabartma tozu ve vanilyayı ekleyip ele yapışmayan bir hamur yoğurun.",
            "Hamurdan ceviz büyüklüğünde parçalar koparıp yuvarlayın ve tepsiye dizin.",
            "180 derece fırında kızarana kadar pişirin, fırından çıkar çıkmaz soğuk şerbeti dökün."
        ])
    },
    {
        "tarif_adi": "Atayef Krep Tatlısı",
        "sure": 30,
        "kategori": "Tatlı Tarifleri",
        "gorsel_url": f"{base_url}/resim/atayef-tarifi.webp",
        "ozet": "Ortadoğu mutfağından gelen, içi krema dolgulu nefis ve şık sunumlu özel krep tatlısı.",
        "malzemeler": json.dumps(["2 su bardağı un", "Yarım su bardağı irmik", "2.5 su bardağı ılık su", "1 tatlı kaşığı maya", "200ml krema", "2 su bardağı süt"]),
        "adimlar": json.dumps([
            "Un, irmik, su, şeker ve mayayı pürüzsüz kıvam alana kadar çırpıp 20 dakika dinlendirin.",
            "Kepçe yardımıyla tavaya döküp kreplerin sadece tek yüzünü pişirin.",
            "Soğuyan kreplerin uçlarını yarım ay şeklinde kapatarak cep yapın.",
            "İçini çırpılmış krema ile doldurup fıstık tozu ile süsleyin."
        ])
    },

    # --- SALATA TARİFLERİ ---
    {
        "tarif_adi": "Geleneksel Kısır",
        "sure": 20,
        "kategori": "Salata Tarifleri",
        "gorsel_url": f"{base_url}/resim/kisir-tarifi.webp",
        "ozet": "Bol yeşillik ve nar ekşisiyle harmanlanmış, damaklarda iz bırakan nefis geleneksel Hatay kısırı.",
        "malzemeler": json.dumps(["2 su bardağı ince bulgur", "2 yemek kaşığı salça (biber/domates)", "Yarım demet taze soğan, maydanoz, nane", "Yarım çay bardağı zeytinyağı", "Nar ekşisi, limon suyu, tuz"]),
        "adimlar": json.dumps([
            "İnce bulguru derin bir kaba alıp üzerini geçecek kadar sıcak su ile ıslatın ve dinlendirin.",
            "Şişen bulgura domates ve biber salçasını ekleyip rengi dönene kadar iyice yoğurun.",
            "İnce kıyılmış taze soğan, maydanoz ve naneyi ilave edin.",
            "Zeytinyağı, limon suyu, nar ekşisi ve baharatları ekleyip iyice harmanlayın.",
            "Taze marul yaprakları ile servis edin."
        ])
    },
    {
        "tarif_adi": "Avokadolu Karides Salatası",
        "sure": 15,
        "kategori": "Salata Tarifleri",
        "gorsel_url": f"{base_url}/resim/avakadolu-karides-salatasi-tarifi.webp",
        "ozet": "Taze deniz ürünleri ve avokadonun ferahlatıcı uyumuyla hazırlanan sağlıklı, hafif ve şık gurme salata.",
        "malzemeler": json.dumps(["300g haşlanmış karides", "2 adet olgun avokado", "1 adet mor soğan", "Akdeniz yeşillikleri", "Zeytinyağı, limon suyu, hardal"]),
        "adimlar": json.dumps([
            "Karidesleri ayıklayıp hafifçe haşlayın veya tereyağında soteleyin.",
            "Avokadoları ve mor soğanları küp küp doğrayın.",
            "Akdeniz yeşilliklerini geniş bir kaseye alın.",
            "Üzerine avokado, soğan ve karidesleri ekleyin.",
            "Zeytinyağı, limon ve hardal ile hazırladığınız sosu gezdirerek servis yapın."
        ])
    },

    # --- KAHVALTILIK ---
    {
        "tarif_adi": "Çiçek Yumurta (Sunumluk)",
        "sure": 10,
        "kategori": "Kahvaltılık",
        "gorsel_url": f"{base_url}/resim/cicek-yumurta-tarifi.webp",
        "ozet": "Kahvaltı sofralarınızı görsel bir şölene çevirecek, kırmızı kapya biber halkaları içinde sunumluk nefis yumurta.",
        "malzemeler": json.dumps(["2 adet kalın kesilmiş kırmızı kapya biber", "2 adet yumurta", "1 tatlı kaşığı tereyağı", "Tuz, karabiber", "Çörek otu"]),
        "adimlar": json.dumps([
            "Kırmızı kapya biberleri kalın halkalar halinde kesin.",
            "Tavada tereyağını eritip biber halkalarını tavaya yerleştirin.",
            "Her bir biber halkasının içine birer yumurta kırın.",
            "Tuz, karabiber ve çörek otu serpiştirin.",
            "Yumurtalar istediğiniz kıvama gelene kadar pişirip servis tabağına alın."
        ])
    },
    {
        "tarif_adi": "Yeşil Soğanlı Kalp Yumurta",
        "sure": 10,
        "kategori": "Kahvaltılık",
        "gorsel_url": f"{base_url}/resim/yesil-soganli-kalp-yumurta-tarifi.webp",
        "ozet": "Taze yeşil soğanlarla kalp şekli verilmiş, kahvaltılarınıza sevgi katacak pratik ve şık sunum.",
        "malzemeler": json.dumps(["2 adet yumurta", "3 dal taze yeşil soğan", "1 tatlı kaşığı tereyağı", "Tuz, pul biber"]),
        "adimlar": json.dumps([
            "Taze yeşil soğanları ikiye katlayarak tavada kalp şekli verin.",
            "Tavaya tereyağı ekleyip soğanları hafifçe soteleyin.",
            "Yumurta dikkatlice soğan kalplerinin ortasına kırın.",
            "Tuz ve pul biber serpiştirip kapağını kapatarak pişmeye bırakın."
        ])
    }
]

df = pd.DataFrame(veri)
df.to_csv('recipes.csv', index=False, encoding='utf-8')
print("Veri setindeki tüm görseller her yemeğe özel orijinal .webp dosyalarıyla güncellendi!")