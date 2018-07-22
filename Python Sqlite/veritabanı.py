import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()

def veri_ekle():
    cursor.execute("INSERT INTO kitaplık VALUES('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()

def veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("INSERT INTO kitaplık VALUES(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()

def verileri_al():
    cursor.execute("Select * From kitaplık")
    liste = cursor.fetchall()
    print("Kitaplık tablosunun bilgileri...")
    for i in liste:
        print(i)

def verileri_al2():
    cursor.execute("Select İsim,Yazar From kitaplık")
    liste = cursor.fetchall()
    print("Kitaplık tablosunun bilgileri...")
    for i in liste:
        print(i)

def verileri_al3():
    cursor.execute("Select * From kitaplık where yayınevi='everest'")
    liste = cursor.fetchall()
    print("Kitaplık yayınevi everest olan tablosunun bilgileri...")
    for i in liste:
        print(i)

def verileriguncelle(eski_yayınevi,yeni_yayınevi):
    cursor.execute("Update kitaplık set yayınevi= ? where yayınevi = ? ",(yeni_yayınevi,eski_yayınevi))
    con.commit()


def verilerisil(yazar):
    cursor.execute("Delete From kitaplık where yazar = ?",(yazar,))
    con.commit()

verilerisil("Ahmet Ümit")
#verileriguncelle("doğan kitap","everest")
#verileri_al3()
#verileri_al2()
#verileri_al()

#isim = input("İsim:")
#yazar = input("Yazar:")
#yayınevi = input("Yayınevi:")
#sayfa_sayısı = int(input("Sayfa Sayısı:"))
#veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı)

con.close()
