okul=("sancaktepe taihl")
#tüm karakterleri büyük yap:upper
print(okul.upper())

#tüm karakterleri küçük yar:lower
print(okul.lower())

#Her kelimenin ilk harfini büyük yap:title

print(okul.title())

#Karakter dizisinin ilk karakterini büyük diğer karakterlerini küçük yap:capitalize
print(okul.capitalize())

#Belirli bir ifadenin kaç defa yer aldığını bulalım:count
print(okul.count("e"))
makale=("son yüzyıllarda teknolojinin insanlara neler kazandırdığını, ne gibi faydaları olduğunu anlatmak için sayfalar yetersiz kalır. Sadece televizyon ve bilgisayarın faydaları bile, teknolojinin hayatımıza katkılarını özetlemeye yeter. Doğrudan ve dolaylı olarak insanlara on binlerce faydasından söz edebiliriz. "
        "Bazıları şunlar;Teknoloji sayesinde bilgi alışverişi kolaylaştı. Dünyanın öteki ucunda gerçekleşen bir olaydan anında haberimiz oluyor.Hayatı kolaylaştırır ve pratikleştirir. Evinizde internetten alışveriş yapabilirsiniz, kilometrelerce uzaklıktaki bir olayı anlık olarak izleyebilirsiniz, 2 dakikada apartmanın 10. katına çıkabilirsiniz.Günümüzde tıp sektörü neredeyse her alanda teknolojiye bağımlı. DNA analizleri, tahliller, ameliyatlar gibi sayısız tıp uygulaması teknoloji sayesinde gerçekleşebilir.Ölümcül birçok hastalığın çaresi teknoloji sayesinde bulunmuştur.")


print(makale.lower().count("teknoloji"))

#soldaki ve sağdaki boşluk karakterlerini temizleyelim:strip()
ad=input("adınız:")
print(ad.strip())

#Soldaki ve sağdaki karakterleri temizleyelim:strip("ifade")
urun_kodu="hep20221022hep"
print(urun_kodu.strip("hep"))

#Soldaki boşluk veya belirli ifadeyi temizleyelim:lstrip
print(ad+"|")#adı boşluklara gönder
print(urun_kodu.lstrip("hep")+("|"))
print(urun_kodu.rstrip("hep"))


#karakter dizisini bölelim:split()
print(okul.split())

#Böldüğümüz ve listeye dönüşen ifadeleri birleştirelim:join
kelimeler= okul.split()
print(kelimeler)
print("---".join(kelimeler))


#ortalayıp çıktı verme:center
print("Muhsin".center(25,"-"))