# print('merhaba benim adım {}'.format("eren"))
# print('merhaba benim adım {0},yasim {1}'.format("eren",21))
# print('merhaba benim adım {1},yasim {0}'.format("eren",21))
# print('merhaba benim adım {ad},yasim {yas}'.format(ad="eren",yas=21))

# ders 2 ---------------------------------------------------------------

# sayi =11
# print(sayi)
# sayi=sayi+4
# print(sayi)

# ders 3 ---------------------------------------------------------------

# print(type(2))

# ders 4 ---------------------------------------------------------------

# strvar = "python"
# print(len(strvar))  
# print(strvar[2:])
# print(strvar.upper())

#ders 6 ----------------------------------------------------------------

# sayilar=[1,1,3,657,876,898,5676]
# sayilar.sort()
# print(sayilar)

# sayilar.reverse()
# print(sayilar)

# print(set(sayilar))

# "tup veri tipi değiştirilemez"
# "count kaç tane var olduğunu sorgulamak için kullanılır  orn: list.count('a')"

# ders 7 -----------------------------------------------------------------

# dict={
#     'isim':"eren",
#     'yas':21,
#     'yasadiği yer':"trabzon"
# }
# print(dict)
# print(dict.get("yas"))
# print(dict['yasadiği yer'])

# ders 8 ------------------------------------------------------------------

# hava_durumu='karli'
# if hava_durumu=='soguk':
#     print('mont giyin')

# elif hava_durumu=='karli':
#     print('atki al')

# else:
#     print('tamam')

# liste=['a',3,5,'h']
# hedef_char='f'
# if hedef_char in liste:
#     print('mevcut')
# else:
#     liste.append(hedef_char)
#     print('yoktu ama eklendi !')
#     print('Güncel liste {}'.format(liste))     
    
# ders 9 -------------------------------------------------------------------

# yorum_birakanlar=['eren demircan','yusuf can dursun','memet ali erbil','ahmet balaban']
# for isimler in yorum_birakanlar:
#     print('\n',isimler)

# kullanici_sayisi=0
# yorum_birakanlar=['eren demircan','yusuf can dursun','memet ali erbil','ahmet balaban']
# for isimler in yorum_birakanlar:
#     kullanici_sayisi=kullanici_sayisi+1
#     print(kullanici_sayisi,isimler) 

# dict={
#     'ad':'eren',
#     'soyad': 'demircan'
# }
# print(dict.items())
# for x,y in dict.items():
#     print('Key:{} ,\t Value: {}'.format(x,y))
  
# ders 10 --------------------------------------------------------------------

# print(range(10))
# print([*range(10)])  # alttakiyle aynı
# print(list(range(10)))
# print('---------------------------------\n')

# for sayi in range(5):
#     print(sayi)

# print('---------------------------------\n')

# harfler=['a','b','c','d','e']
# for indeks,harf in enumerate(harfler):
#     print(indeks+1,harf)
# print('---------------------------------\n')
# ulkeler=['TR','AZE','FR']
# siralamalar=range(1,4) 
# for ulke in zip(siralamalar,ulkeler):
#     print(ulke)   

# ders 11 ------------------------------------------------------------------

# harfler=['a','b','c','d','e']*10
# for indeks,harf in enumerate(harfler):
#     if harf=='c':
#         print('{} harfi {}. indekste'.format(harf,indeks))
#         break


# for sayi in range(1,8):
#     if sayi%2==0:
#         continue
#     print(sayi)

# print('---------------------------')

# for sayi in range(1,8):
#     if sayi%2==0:
#         pass
#     else:
#         print(sayi)

# ders 12 ------------------------------------------------------------------
    
# def fonksiyon():
#     print(5)
# def fonksiyon1():
#     print('a')
# fonksiyon1()    


# def buyuk_sayi_dondur(a,b):
#     if a<b:
#         return b
#     elif a>b:
#         return a
# def metin_yazdir(a,b):
#     buyuk_sayi=buyuk_sayi_dondur(a,b)
#     sablon_metin="{} daha buyuk bir sayidir".format(buyuk_sayi)
#     print(sablon_metin)
    
# metin_yazdir(10,5)

# ders 13 ------------------------------------------------------------------

# def karesini_al(x):
#     return x**2

# sayilar=[*range(1,6)]       #map bir fonksiyonu listenin her elemanina uygulamasini saglar
# print( [ * map ( karesini_al,sayilar ) ] )
# print( [*map(lambda sayi: sayi**2,sayilar)])   #lambda ise algoritma yolunu gösterek yapmış oluyor



# def cift_sayilari_listele(x):
#     return x if x%2==0 else None

# sayilarim=[*range(1,6)]
# print([*filter(cift_sayilari_listele,sayilarim)])




# girdi=input("Bir mesaj giriniz")
# print(girdi)


# def sayi_deger():
#      girdi =input("bir sayi giriniz: ")

#      while not girdi.isdigit():
#            print(  "girdiğiniz değer sayi tipinde değildir")
#            girdi=input("bir değer giriniz: ")
#     #  if girdi.isdigit():
#     #       print( "tebrikler sayi tipinde bir deger girdiniz")


#      else:
#         #  print(  "girdiğiniz değer sayi tipinde değildir")
#          print( "tebrikler sayi tipinde bir deger girdiniz")
     
# sayi_deger()     





# def eposta_kontrol():
#     girdi=input(" Geçerli bir  e-posta edresi giriniz. ")

#     while not (('.' in girdi) and ('@' in girdi)):
#         print("Geçerli bir e-posta girmediniz!")
#         girdi=input(" Geçerli bir  -posta edresi giriniz. ")

#     else:
#         print("Tebrikler geçerli bir e-postayla girişiniz yapıldı!")

# eposta_kontrol()


# ders 14 ------------------------------------------------------------------


# def tam_sayiya_cevir():                                                   #round
#     girdi=input("Bir ondalık sayı giriniz: ")
#     print("{} bu tam sayıya yuvarlandı ".format(round(float(girdi))))
# tam_sayiya_cevir()



# def tam_sayiya_cevir():
#     girdi=input("Bir ondalık sayı giriniz: ")
#                                                                          #try-except
#     try:
#         girdi=float(girdi)
#         print("Tam sayıya yuvarlanan ifade {} ".format(round(girdi)))
#     except:
#         print("{} tam sayiya çevirilemeyen ifade".format(girdi))    
# tam_sayiya_cevir()



# def tam_sayiya_cevir():
#     girdi=input("Bir ondalık sayı giriniz: ")
#     status=''
                                                                         
#     try:                                                         #finally
#         girdi=float(girdi)
#         print("Tam sayıya yuvarlanan ifade {} ".format(round(girdi)))
#         status='basarili'
#     except:
#         print("{} tam sayiya çevirilemeyen ifade".format(girdi))    
#         status='basarisiz'
#     finally:
#         print("Çevirme işlemi {} olarak gerçekleşti".format(status))    
# tam_sayiya_cevir()




# def tam_sayiya_cevir():
#     while True:
#         girdi=input("Bir ondalık sayı giriniz: ")
#         status=''
#         try:                                                         
#             girdi=float(girdi)
#             print("Tam sayıya yuvarlanan ifade {} ".format(round(girdi)))
#             status='basarili'
#         except:
#             print("{} tam sayiya çevirilemeyen ifade".format(girdi))    
#             status='basarisiz'
#         finally:
#             print("Çevirme işlemi {} olarak gerçekleşti".format(status))    
#             pass
# tam_sayiya_cevir()



# class Ucus():
#     hava_yolu="Thy"

#     def __init__(self,kod,kalkis,varis,sure,kapasite,yolcu):
#         self.kod=kod
#         self.kalkis=kalkis
#         self.varis=varis
#         self.sure=sure
#         self.kapasite=kapasite
#         self.yolcu=yolcu

# ucus2=Ucus(11 , 12.20 , 15.20 , 1.30 , 150 , 123)
# print("yolcu sayisi: " , ucus2.yolcu)


class Ucus():
    hava_yolu="Thy"

    def __init__(self,kod,kalkis,varis,sure,kapasite,yolcu):
        self.kod=kod
        self.kalkis=kalkis
        self.varis=varis
        self.sure=sure
        self.kapasite=kapasite
        self.yolcu=yolcu

    def anons_yap(self):
        return "{} sefer sayili uçuş için bekleniyorsunuz".format(self.kod)
    
    def koltuk_sayisi(self):
        return self.kapasite - self.yolcu
    
    def bilet_satisi(self,bilet_Sayisi=1):    
        if self.yolcu + bilet_Sayisi<=self.kapasite:
            self.yolcu += bilet_Sayisi
            self.koltuk_sayisi()
            return ('{} adet bilet satilmiştir, kalan koltuk sayisi {} adettir'.format(bilet_Sayisi,self.koltuk_sayisi()))
        else:
            return ('İşlem gerçekleştirilemedi!')

    def bilet_iptal(self,bilet_Sayisi=1):
        if self.yolcu-bilet_Sayisi>=bilet_Sayisi:
            self.yolcu -=bilet_Sayisi
            return ('{} adet bilet iptal edilmiştir, güncel koltuk sayisi {} adettir'.format(bilet_Sayisi,self.koltuk_sayisi()))
        else:
            return ('İşlem olmadı!')




ucus1=Ucus('TK12385','IST','ANK',100 , 180 , 130)
print(ucus1.koltuk_sayisi(),'adet boş koltuk vardır')
print(ucus1.bilet_satisi(10))
print(ucus1.bilet_satisi(20))
print(ucus1.bilet_satisi(25))
print(ucus1.koltuk_sayisi())
print(ucus1.bilet_iptal(10))
print(ucus1.bilet_iptal(100))


    
