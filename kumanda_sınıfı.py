import random
import time

class Kumanda():

    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_listesi=["Trt"],kanal="Trt"):

        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal = kanal
    def tv_ac(self):
        if(self.tv_durum=="Açık"):
            print("Televizyon zaten açık")
        else:
            print("Televizyon açılıyor")
            self.tv_durum="Açık"
    def tv_kapat(self):
        if (self.tv_durum=="Kapalı"):
            print("Televizyon zaten Kapalı")
        else:
            print("Kapatılıyor")
            self.tv_durum="Kapalı"
    def ses_ayarları(self):
        while True:
            cevap=input("Sesi azalt: '<'\nSesi Artır: '>'\n Çıkış: çıkış")

            if (cevap=="<"):
                if (self.tv_ses!=0):
                    self.tv_ses -= 1
                    print("Ses: ",self.tv_ses)
            elif (cevap ==">"):
                if (self.tv_ses!=31):
                    self.tv_ses += 1
                    print("Ses: ",self.tv_ses)
            else:
                print("Ses Güncellendi: ",self.tv_ses)
                break
    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)

        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi....")
    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele]
        print(f"Şu anki kanal: {self.kanal}")
    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return f"Tv durumu: {self.tv_durum}\n Tv Ses: {self.tv_ses}\nKanal Listesi: {self.kanal_listesi}\nŞuanki Kanal: {self.kanal}"
kumanda=Kumanda()
print("""
Televizyon uygulaması
1.Tv Aç
2.Tv Kapat
3.Ses Ayarları
4.Kanal Ekle
5.Kanal Sayısını öğrenme
6.Rastgele Kanala Geçme
7.Televizyon Bilgileri
""")

while True:

    işlem=input("İşlemi seçiniz: ")
    if işlem=="1":
        kumanda.tv_ac()
    elif işlem == "2":
        kumanda.tv_kapat()
        break
    elif işlem == "3":
        kumanda.ses_ayarları()
    elif işlem == "4":
        kanal_isimleri=input("Kanal isimlerini ',' ile ayırarark girin:")
        kanal_listesi=kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif işlem == "5":
        print(len(kumanda))
    elif işlem == "6":
        kumanda.rastgele_kanal()
    elif işlem == "7":
        print(kumanda)
    else:
        print("Geçersiz işlem...")




