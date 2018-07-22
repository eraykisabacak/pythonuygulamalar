from kütüphane import *

print("""
***************************************


Kütüphane Programına Hoşgeldiniz.

İşlemler;

1. Kitapları Göster

2. Kitapları Sorgulama

3. Kitap Ekle

4. Kitap Sil

5. Baskı Yükselt

Çıkmak için 'q' ya basın


***************************************""")

kütüphane = Kütüphane()

while True:
    işlem = input("Yapacağınız İşlem:")

    if(işlem == "q"):
        print("Program Sonlandırılıyor...")
        print("Yine Bekleriz")
        break

    elif(işlem == "1"):
        kütüphane.kitapları_goster()

    elif (işlem == "2"):
        isim = input("Hangi Kitabı istiyorsunuz?")
        print("Kitap Sorgulanıyor")
        time.sleep(2)
        kütüphane.kitap_sorgula(isim)

    elif (işlem == "3"):
        isim = input("Kitabın ismi?:")
        yazar = input("Yazarın ismi?:")
        yayınevi = input("Yayınevi ismi?:")
        tür = input("Tür:")
        baskı = int(input("Baskı:"))

        yeni_kitap = Kitap(isim,yazar,yayınevi,tür,baskı)

        print("Kitap ekleniyor")
        time.sleep(2)

        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi")

    elif (işlem == "4"):
        isim = input("Hangi kitabı silmek istiyorsunuz ?:")

        cevap = input("Emin misiniz ? (E/H)")
        if(cevap == "E"):
            print("Kitap siliniyor")
            time.sleep(2)
            kütüphane.kitap_sil(isim)
            print("Kitap silindi")

    elif (işlem == "5"):
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz?")
        print("Baskı yükseltiliyor")
        time.sleep(2)
        kütüphane.baskı_yükselt(isim)
        print("Baskı yükseltildi")
    else:
        print("Geçersiz İşlem")


































