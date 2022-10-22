#boş bir liste tanımlama
liste = []
print(liste)
print(type(liste))
okul="sancaktepe taihl"
kelimeler=okul.split()
print(kelimeler)

#belirli sıradaki kelimeleri yazdıralım
print(kelimeler[0])#ilk kelime
print(kelimeler[1])
print(kelimeler[-1])#son kelime
print(kelimeler[-2])#ilk kelime

ad="muhsin emre kullemci"
print(ad[0])
print(ad[5:12])
print(ad[5:12:2])


#listeler içerisinde farklı türden veriler olabilir
liste=[1,12.3,"python",True,[1,2,3]]
print(liste[-1][-1])#3
print(liste[4][-1])#3
print(liste[4][2])#3

#iki listeyi birleştirme
liste2=[1,2,3]
liste3=[4,5,6]
liste4=liste3+liste2
liste5=liste2+liste3
print(liste4)
print(liste5)