"""
Dictionary "anahtar", "değer" ikililerinden oluşur
    "ad": "Eren"
    "soyad": "Özdal"
"""
#belirli bir numaraya sahip öğrenciyi bulma işlemini liste ile yap
#numaralar=[66,75]
#isimler=["ahmet","mehmet"]
#numara=int(input("Öğrenci numarasını yaz:"))
#konum=numaralar.index(numara)
#print(isimler(konum))

#belirli bir numaraya sahip öğrenciyi bulma işlemini dictionary ile yapalım
#ogrenciler = {66:"ahmet",75:"mehmet"}
#print(ogrenciler[numara])

#detaylı örnek
kisiler = {
    1:{
        "ad":"Muhsin",
        "soyad":"Kullemci",
        "cinsdiyet":True,
        "dersler":["Türkçe","Matematik","Fen"]

    },
    45:{
        "ad":"Mahmut",
        "soyad":"Kullemci",
        "cinsiyet":True,
        "dersler":["Türkçe","Matematik","Fen"]
    },



}

#45 numaralı öğrencinin derslerini yazdır
print(kisiler[45]["dersler"])