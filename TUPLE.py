liste=[1,2,3]
tuple=("bir","iki","üç")

#tuple'ı ekrana yazdıralım
print(liste)
print(type(liste))
print(tuple)
print(type(tuple))
#belirli bir elemanı ekrana yazdıralım
print(tuple[0])

#listenin ve tuplenin bir elemanını değiştir
liste[0] =7
print(liste)
#TypeError: 'tuple' object does not support item assignment
#tuple[0]="yedi" hata verdi
print(tuple)

#tuple içindeki belirli bir elemanın indeksini bul:index()
print(tuple.index("iki"))

#2 tuple'ı birleştirelim
tuple=(1,2,3)
tuple2="bir","iki","üç"
print(tuple+tuple2)