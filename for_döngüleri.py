#ogrenciler=["mehmet","ali","veli"]

#for ogrenci in ogrenciler:
#    print(f"Öğrencinin adı: {ogrenci}")


#sayilar=[(1,2),(3,4),(5,6)]
#for a, b in sayilar:
#    print(f"1.sayı:{a},2.sayı:{b}")


okul_adi="Sancaktepe teknoloji anadolu imam hatip lisesi"
kelimeler=okul_adi.split()
for kelimeler in kelimeler:
    print(f"kelime: {kelimeler}")



ogrenciler={
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

for no,ogrenci in ogrenciler.items():
    print(f"{no} numaralı öğrenci: {ogrenci['ad']}")