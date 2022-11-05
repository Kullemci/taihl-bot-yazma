sayılar = [9,21,56,78,34,52,98,76,27,64,623]
harfler = ["a","g","r","d","b","j","p","n","t","j","w","q","x","h","o"]

#listelerin eleman sayısını bul:len(liste)
#print(len(harfler+sayılar))


#listenin en küçük değerli elemanını bul:min
#print(min(sayılar))
#print(min(harfler))

#listenin en büyük değerli elemannı bul:max()
#print(max(sayılar))
#print(max(harfler))

#metin ve sayılardan oluşan listeleri birleştirip en büyüğünü bulalım
#birlesmis=sayılar+harfler
#print(max(birlesmis))
#TypeError: '>' not supported between instances of 'str' and 'int'(int ve str büyük küçük olarak karşılaştırılamaz)

#listenin sonuna eleman ekle:append()
#sayılar.append(32)
#print(sayılar)

#listenin istediğimiz konumuna yeni eleman ekleyelim:insert()
#harfler.insert(3,"b")
#print(harfler)

#listenin sonundaki elemanı silelim:pop()
#harfler.pop()
#print(harfler)
#harfler.pop(3)#belirli konumdaki b harfi sildi
#print(harfler)

#listede belirli bir değere sahip elemanları sil:remove("değer")
#harfler.append("a")
#print(harfler)
#harfler.remove("a")
#print(harfler)

#listedeki elemanları sırala:sort
print(sayılar)
sayılar.sort()
sayılar.reverse()
print(sayılar )
sayılar.sort(reverse=True)#tersten yzaar
print(sayılar)
print("-"*50)#aayraç

print(harfler)
harfler.sort()
harfler.reverse()
print(harfler )
harfler.sort(reverse=True)#tersten yzaar
print(harfler)

#Listdeki isimleri alfabetik sıraya göre sıralıyalım
isimler=["muhsin","talha","emirhan"]
isimler.sort()
print(isimler)

#listeyi temizleme:clear()
isimler.clear()
print(isimler)

