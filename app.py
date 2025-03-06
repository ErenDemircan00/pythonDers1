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

kullanici_sayisi=0
yorum_birakanlar=['eren demircan','yusuf can dursun','memet ali erbil','ahmet balaban']
for isimler in yorum_birakanlar:
    kullanici_sayisi=kullanici_sayisi+1
    print(kullanici_sayisi,isimler)
  