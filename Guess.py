import random

flag = True
while flag:
    num = input("Lütfen üst sınırı giriniz: ")

    if num.isdigit():
        print("Hadi başlayalım")
        num = int(num)
        flag = False
    else:
        print("Lütfen sayı giriniz!")

secim = random.randint(1,num)

tahmin = None
count = 1

while tahmin != secim:
    tahmin = input('Lütfen 1 ve ' + str(num) + ' arasında sayı giriniz: ')
    if tahmin.isdigit():
        tahmin = int(tahmin)
    if tahmin < secim:
        print('Lütfen tahmininizi arttırın!')
    if tahmin > secim:
        print('Lütfen tahmininizi azaltın!')
    if tahmin == secim:
        print('Tebrikler ' + str(count) + ' tahminde sayıyı buldunuz!')
    else:
        print('Tekrar deneyin!')
        count += 1
input("ENTER tuşuna basarak çıkış yapabilirsiniz...")
"""
while tahmin != secim:
    tahmin = input('Lütfen 1 ve ' + str(num) + ' arasında sayı giriniz: ')
    if tahmin.isdigit():
        tahmin = int(tahmin)
    if tahmin == secim:
        print('Sayıyı buldunuz!')
    else:
        print('Tekrar deneyin!')
        count += 1
print(str(count) + ' tahminde buldunuz!') """