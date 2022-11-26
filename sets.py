"""
sets listeleri süslü parantezler '{}' içinde tanımlanır.
sets liste elemanlarına indeks numaraları ile ulaşılamaz.
sets liste elemanlarına döngü içinde ulaşılır.
sets listeleri içinde aynı eleman birden fazla yer alamaz.
"""

#set listesi oluştur
sets_liste={1,2,3,4}

#sets listesinin içindeki elemana ulaş
#print(sets_liste[0]) hata verdi


#sets liste elemanlarna döngü ile ulaş
for eleman in sets_liste:
    print(eleman)

#sets listesinde bir eleman ekle:add()
sets_liste.add(5)
print(sets_liste)



#sets_listesine bir/birden fazla eleman ekle:update([])
sets_liste.update([19,20,21])
print(sets_liste)

#tekrarlayan elemanı olan listeyi sets listesine dönüştür:set()
liste=[1,2,3,4,5,1,6,5,24,32,22,22]
sets_liste=set(liste)
print(sets_liste)