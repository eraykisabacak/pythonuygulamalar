import sqlite3

import time

class Sarki():

    def __init__(self,isim,sanatçı,albüm,prodüksiyon_şirketi,şarkı_süresi):

        self.isim = isim
        self.sanatçı = sanatçı
        self.albüm = albüm
        self.prodüksiyon_şirketi = prodüksiyon_şirketi
        self.şarkı_süresi = şarkı_süresi

    def __str__(self):

        return "Şarkı İsmi : {}\nSanatçi : {}\nAlbüm : {}\nProdüksiyon Şirketi : {}\nŞarkı Süresi : {}".format(self.isim,self.sanatçı,self.albüm,self.prodüksiyon_şirketi,self.şarkı_süresi)


class Sarkilar():

    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("sarkilar.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table If not exists sarkilarım (isim TEXT,sanatçı TEXT,albüm TEXT,prodüksiyon_şirketi TEXT,şarkı_süresi INT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()

    def baglanti_kes(self):
        self.baglanti.close()

    def şarkıları_göster(self):

        sorgu = "Select * From sarkilarım"

        self.cursor.execute(sorgu)

        sarkilarım = self.cursor.fetchall()

        if(len(sarkilarım) == 0):
            print("Şarkı bulunmuyor")
        else:
            for i in sarkilarım:
                sarki = Sarki(i[0],i[1],i[2],i[3],i[4])
                print(sarki)

    def şarkı_sorgula(self,isim):

        sorgu = "Select * From sarkilarım where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        sarkilarım = self.cursor.fetchall()

        if (len(sarkilarım) == 0):
            print("Şarkı bulunmuyor")
        else:
            for i in sarkilarım:
                sarki = Sarki(i[0][0], i[0][1], i[0][2], i[0][3], i[0][4])
                print(sarki)


    def şarki_ekle(self,sarki):

        sorgu = "Insert into sarkilarım Values(?,?,?,?,?)"

        self.cursor.execute(sorgu,(sarki.isim,sarki.sanatçı,sarki.albüm,sarki.prodüksiyon_şirketi,sarki.şarkı_süresi))

        self.baglanti.commit()

    def şarkı_sil(self,isim):

        sorgu = "Delete From sarkilarım where isim = ?"

        self.cursor.execute(sorgu(isim,))

        self.baglanti.commit()





























