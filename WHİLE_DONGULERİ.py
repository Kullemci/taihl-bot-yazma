#sayi=0
#while sayi <101:
  #  print(sayi)
  #  sayi +=1
   # if sayi%2==0 :
    #    print("Çift sayı")

    #else:
      #  print("tek sayıdır")

import xlrd
ck=xlrd.open_workbook("veriler/WorldCupPlayers.xls")


#excel çalışma sayfasını aç
cs=ck.sheet_by_index(0)

#toplam satır sütun sayısını yazdır
satir_sayisi = cs.nrows
sutun_sayisi = cs.ncols
print(f"Satır sayısı:{satir_sayisi}")
print(f"Sütün sayısı:{sutun_sayisi}")

#ilk bailık satırı
a1 = cs.cell(0,0)
print(a1)

satir=1# başlıkları es geçmek için 1. indeks den başla

while satir<satir_sayisi:
    futbolcu=cs.cell_value(satir,6)
    #print(futbolcu)


    #if futbolcu.startswith("R"):
     #   print(f"Futbolcu: {futbolcu}")


     #bir olay yaşamış oyuncular
    olay=cs.cell_value(satir,8)
    if olay !="":
        print(f"futbolcu:{futbolcu}-olay:{olay}")
    satir += 1