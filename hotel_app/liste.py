import sqlite3
veritabani=sqlite3.connect("hotel.db")
imlec=veritabani.cursor()
hotel = """CREATE TABLE IF NOT EXIST clientRegis (ad,soyad,numara)"""



def müsterikaydi(ad,soyad,numara,kimlik,personalThing,clientList):
    personalThing.clear()
    ad=input("Adınızı giriniz.\n")
    personalThing.append(ad)
    soyad=input("Soyad giririniz.\n")
    personalThing.append(soyad)
    numara=input("Telefon numaranızı giriniz.\n")        
    kimlik=input("Kimlik numaranızı giriniz.\n")
    personalThing.append(numara)
    clientList.append(personalThing)

    imlec.execute("""insert into clientRegis(clientName,clientSurname,clientPhone,clientId)
        values(?,?,?,?)""",[ad,soyad,numara,kimlik])
    veritabani.commit()







def genelRapor(clientList,ucretToplam,ucretOda,ucretSauna,kisiToplam,kisiOda,kisiSauna):
    print(clientList)
    print("Toplam kazanç:\n",ucretToplam,"TL")
    print("Odalardan elde edilen kazanç:\n",ucretOda,"TL")
    print("Saunadan elde edilen kazanç:\n",ucretSauna,"Tl")
    print("Toplam müşteri:\n",kisiToplam)
    print("Oda hizmeti alan müşteri:\n",kisiOda)
    print("Sauna hizmeti alan müşteri:\n",kisiSauna)