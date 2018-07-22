from şarkı import *

print("""
***************************************


Şarkılarım Programına Hoşgeldiniz

İşlemler;

1. Şarkıları Göster

2. Şarkıları Sorgulama

3. Şarkı Ekleme

4. Şarkı Sil

Çıkmak için 'q' ya basın


***************************************""")

şarkı = Sarkilar()

while True:

    işlem = input("Yapacağınız İşlem:")

    if(işlem == "q"):
        print("Program Sonlandırılıyor...")
        print("Yine Bekleriz")
        break

    elif(işlem == "1"):
        şarkı.şarkıları_göster()

    elif (işlem == "2"):
        isim = input("Hangi Şarkıyı İstiyorsunuz")
        print("Kitap Sorgulanıyor")
        time.sleep(2)
        şarkı.şarkı_sorgula(isim)

    elif (işlem == "3"):
        isim = input("Şarkının ismi?:")
        sanatçı = input("Sanatçının ismi?:")
        albüm = input("Albüm ismi?:")
        prodüksiyon_şirketi = input("Prodiksiyon Şirketi:")
        şarkı_süresi = int(input("Şarkı Süresi:"))

        yeni_sarki = Sarki(isim,sanatçı,albüm,prodüksiyon_şirketi,şarkı_süresi)

        print("Kitap Ekleniyor")
        time.sleep(2)

        şarkı.şarki_ekle(yeni_sarki)
        print("Kitap eklendi")

    elif (işlem == "4"):
        isim = input("Hangi Şarkıyı Silmek istiyorsunuz")

        cevap = input("Emin Misiniz ? (E/H)")
        if(cevap == "E"):
            print("Kitap Siliniyor")
            time.sleep(2)
            şarkı.şarkı_sil(isim)
            print("Şarkı Silindi")
    else:
        print("Geçersiz İşlem")





















































