
"""
MANTIKSAL OPERATÖRLER
//////////////////////////////////////////////////////////////////////////////
Python'da birden fazla koşulu beraber değerlendirmek için kullanırız.
+----------+----------+-----------------+
| Operatör | Açıklama |    Kullanımı    |
+----------+----------+-----------------+
|    and   | ve       | (x<y) and (a>b) |
+----------+----------+-----------------+
|    or    | veya     |  (x<y) or (a>b) |
+----------+----------+-----------------+
|    not   | değil    |    not (x<y)    |
+----------+----------+-----------------+
"""

# fulbolcuların 5 gol ve 8 asist üzerinde olanları başarılı sayalım
messi={
    "gol":5,
    "asist":9
}
ronaldo={
    "gol":8,
    "asist":10
}

print(f"messi:{(messi['gol']>5 and messi['asist']>8)}")
print(f"messi:{(ronaldo['gol']>5 and ronaldo['asist']>8)}")

#futbolcuların golü 5'ten fazlaysa veya asisti 8'den fazlaysa başarılı sayalım
print(f"messi:{(messi['gol']>5 or messi['asist']>8)}")
print(f"messi:{(ronaldo['gol']>5 or ronaldo['asist']>8)}")

#futbolcunun golü 5den büyük değilse başarısız olsun
print(f"messi:{not(messi['gol']>5)}")
print(f"ronaldo:{not(ronaldo['gol']>5)}")