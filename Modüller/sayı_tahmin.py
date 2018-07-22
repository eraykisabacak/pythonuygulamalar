import random
import time

print("""
************************

Sayı Tahmin Oyunu


1 ile 40 arasında sayıyı tahmin edin.


************************
""")

rasgele_sayı = random.randint(1,40)
tahmin_hakkı = 7

while True:
    tahmin = int(input("Tahmininiz:"))

    if(tahmin < rasgele_sayı):
        print("Bilgiler Sorgulanıyor")
        time.sleep(1)
        print("Bilgiler Sorgulanıyor.")
        time.sleep(1)
        print("Bilgiler Sorgulanıyor..")
        time.sleep(1)
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)

        print("Daha yüksek sayı yazın")

        tahmin_hakkı -= 1
    elif (tahmin > rasgele_sayı):
        print("Bilgiler Sorgulanıyor")
        time.sleep(1)
        print("Bilgiler Sorgulanıyor.")
        time.sleep(1)
        print("Bilgiler Sorgulanıyor..")
        time.sleep(1)
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)

        print("Daha düşük sayı yazın")

        tahmin_hakkı -= 1
    elif(tahmin == rasgele_sayı):
        print("Bilgiler Sorgulanıyor")
        time.sleep(1)
        print("Bilgiler Sorgulanıyor.")
        time.sleep(1)
        print("Bilgiler Sorgulanıyor..")
        time.sleep(1)
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)

        print("Tebrikler! Sayımız,",rasgele_sayı)
        break
    if(tahmin_hakkı == 0):
        print("Tahmin Hakkınız Bitti")
        print("Sayımız",rasgele_sayı)
        break

