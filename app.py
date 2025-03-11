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
    
def fonksiyon():
    print(5)
def fonksiyon1():
    print('a')
fonksiyon1()    