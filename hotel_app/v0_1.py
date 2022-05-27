# -*- coding: utf-8 -*-
import sqlite3
veritabani=sqlite3.connect("hotel.db")
imlec=veritabani.cursor()

import liste
personalThing=[]
clientList=[]
fiyatListesi={"Standart":"Standart oda kişilik 100 TL","Lüx":"Lüx oda kişilik 350 TL","Ortak":"Ortak sauna kişi başı 60 TL","Özel":"Özel oda 650 TL"}
stuff={"Bay Sıfır":"Lobi 5421112131","Bay SıfırJR":"Bellboy 5421122232","Bay Mendl":"Pastane 54211111010"}
ad=("")
soyad=("")
numara=("")
kimlik=("")
ucretToplam=0
ucretOda=0
ucretSauna=0
kisiToplam=0
kisiOda=0
kisiSauna=0
password1="unuttum1"
password2="abrakadabra"
odaSayac=1
#gereksiz detay olmasın diye yaş olayına girmedim ileride eklenebilir

class Services:
    def __init__(self,name,price): 
     self.name = name                           
     self.price = price    
    servicesName=""
    servicesPrice=""
services_1 = Services("Standart oda","kişilik 100 TL")
services_2= Services("Lüx oda","kişilik 350 TL")
services_3= Services("Ortak sauna","kişilik 60 TL")
services_4= Services("Özel sauna","oda 650 TL")
print("Hotel servisimize hoşgeldiniz.\n")
while True:
    print("""
     -Fiyat listesi için 1
     -Oda kiralamak için 2
     -Sauna hizmeti için 3
     -Günlük rapor için 4
     -Çalışan numarası için 5
     -Çıkış için 6 tuşlayınız \n""")
    menusecim = input("Seçiminizi Giriniz\n")
    if menusecim == "1":
        print(services_1.name)
        print(services_1.price)
        print(services_2.name)
        print(services_2.price)
        print(services_3.name)
        print(services_3.price)
        print(services_4.name)
        print(services_4.price)
        continue
    elif menusecim == "2":
        print("Standart odalar için 1\nLüx odalar için 2 tuşlayınız.\n")
        odasecim= input("")
        if odasecim== "1":
            liste.müsterikaydi(ad, soyad, numara,kimlik,personalThing,clientList)
            yosayi=0
            cosayi=0
            anlikUcret=0
            anlikKisi=0
            print("Standart oda seçtiniz.")
            gunSayi=input("Kaç gün konaklamak istersiniz\n")
            yosayi=input("Yetişkin sayısı gir\n")
            cosayi=input("Çocuk sayısı giriniz\n")
            try:    
                anlikUcret= gunSayi*((100*yosayi)+(50*cosayi))
                ucretToplam+=anlikUcret
                anlikKisi= yosayi+cosayi
                kisiOda+= yosayi+cosayi
                kisiToplam+=anlikKisi
            except (ValueError,TypeError):
                print("Lütfen sayı giriniz.")
                continue
            print("Ödeyeceğiniz tutar:",anlikUcret,"TL\n")
            print("Müşteri numaranız:",odaSayac,"\n")
            odaSayac+=1
            continue
        elif odasecim=="2":
            liste.müsterikaydi(ad, soyad, numara,kimlik,personalThing,clientList)
            yosayi=0
            cosayi=0
            anlikUcret=0
            anlikKisi=0
            print("Lüx oda seçtiniz.")
            gunSayi=int(input("Kaç gün konaklamak istersiniz\n"))
            yosayi=int(input("Yetişkin sayısı gir\n"))
            cosayi=int(input("Çocuk sayısı giriniz\n"))
            try:
                anlikUcret= gunSayi*((350*yosayi)+(175*cosayi))
                ucretToplam+=anlikUcret
                anlikKisi= yosayi+cosayi
                kisiOda+= anlikKisi
                kisiToplam+=anlikKisi
            except (ValueError,TypeError):
                print("Lütfen sayı giriniz.")
                continue
            print("Ödeyeceğiniz tutar:",anlikUcret,"TL\n")
            print("Müşteri numaranız:",odaSayac,"\n")
            odaSayac+=1
            continue
        else:
            print("Hatalı giriş yaptınız lütfen tekrar tuşlayınız.\n")
            continue
    elif menusecim == "3":
        print("Ortak sauna için 1\nÖzel oda için 2 tuşlayınız.\n")
        saunasecim=input("")
        if saunasecim=="1":
            yskisi=0
            cskisi=0
            yskisi=int(input("Yetişkin sayısı gir.\n"))
            cskisi=int(input("Çocuk sayısı gir.\n"))
            try:   
                anlikUcret=(60*yskisi)+(30*cskisi)
                anlikKisi=yskisi+cskisi
                ucretToplam+=anlikUcret
                kisiSauna+=anlikKisi
                kisiToplam+=anlikKisi    
            except (ValueError,TypeError):
                print("Lütfen sayı giriniz.")
                continue
            print("Ödeyeceğiniz tutar:",anlikUcret,"TL\n")
            continue
        elif saunasecim=="2":
            skisi=0
            skisi=int(input("Özel odayı kullanıcak kişi sayısını giriniz.\n"))
            try:
                ucretToplam=ucretToplam+650
                kisiSauna+=skisi
                kisiToplam+=skisi
            except (ValueError,TypeError):
                print("Lütfen sayı giriniz.")
                continue
            print("Ödeyeceğiniz tutar:650TL\n")
            continue
        else:
            print("Hatalı giriş yaptınız.\n")
            continue
    elif menusecim =="4":
        password1=input("Günlük rapor için şifreyi giriniz.\n")
        if password1 =="unuttum1":
                raporSecim=input("genel rapor için g\nözel bir müşteri için s giriniz.")
                if raporSecim=="g":
                    liste.genelRapor(clientList,ucretToplam,ucretOda,ucretSauna,kisiToplam,kisiOda,kisiSauna)
                    continue
                elif raporSecim=="s":
                    raporS=int(input("Müşteri no gir"))
                    raporS-=1
                    print(clientList[raporS])
                    continue
                else:
                    print("Yanlış giriş yaptınız.")
                    continue
                break
        else:
                print("yanlış şifre girdiniz")
                continue
    elif menusecim=="5":
        for i in stuff.keys():
            print(i,stuff[i])
        continue
    elif menusecim=="6":
        print("Çıkış yapılıyor bizi tercih ettiğiniz için teşekkür ederiz.\n")    
        break
    elif menusecim=="7":
        password2=input("Şifre gir.\n")
        if password2=="abrakadabra":
            kimlik=input("kimlik no gir\n")
            imlec.execute("SELECT * FROM clientRegis WHERE clientId=?",kimlik)
            kimbu=imlec.fetchall()
            veritabani.commit()
            print(kimbu)
            continue
        else:
            print("Hatalı giriş yaptınız sistem kapatılıyor.\n")
            break
      
              
    else:
        print("Hatalı giriş yaptınız.\n")
        continue


    