

import time



def kitap_ekle(kitap_ismi,yazar,yayinevi,tur,versiyon):
    sistem = str(("title : \""+kitap_ismi+"\" - author : \""+yazar+"\" - publisher : \""+yayinevi+"\" - type : \""+tur+"\" - edition : \""+str(versiyon)+"\"\n"))
    dosya = open("kutuphane.txt", "a", encoding="utf-8")  # Dosyayı açtık.
    dosya.write(sistem)  # Dosyanın son satırına yeni kitabımızı ekledik.
    dosya.close()  # Dosyayı kapattık.

def kitaplari_goster():
    dosya = open("kutuphane.txt", "r+", encoding='utf8')  # Dosya açıldı.
    liste = dosya.read().splitlines()  # dosyayı satır satır şekilde listeye yazdırdık.
    dosya.close()  # Dosyayı kapattık.
    num = 1  # Kitabın sıra numarası
    for i in liste:  # Tüm kitapları listeledik.
        print(str(num)+"| Kitap : " + i.split("\"")[1] + " | Yazar : " + i.split("\"")[3] + " | Yayınevi : " + i.split("\"")[5] + " | Tür : " + i.split("\"")[7] + " | Baskı : " + i.split("\"")[9] + " |")
        num+=1
    pass

def kitap_ara(kitap_ismi):
    dosya = open("kutuphane.txt", "r+", encoding='utf8')  # Dosyayı açtık.
    liste = dosya.read().splitlines()  # Dosyayı satır satır şeklinde listeye yazdırdık.
    dosya.close()  # Dosyayıı kapattık.

    for i in liste:  # Tüm satırlardaki kitap isimlerinde girilen ismin olduğunu kontrol ettik.
        if(i.split("\"")[1]==kitap_ismi):  # Eğer aranan kitap kütüphanemizde varsa ekrana bastırdık.
            print("Kitap Bulundu.")
            print("| Kitap : "+i.split("\"")[1]+" | Yazar : "+i.split("\"")[3]+" | Yayınevi : "+i.split("\"")[5]+" | Tür : "+i.split("\"")[7]+" | Baskı : "+i.split("\"")[9]+" |")
            return 0

    print("*** Kitap Bulunamadı. ***")
    return 0

def kitap_sil(kitap_ismi):

    dosya = open("kutuphane.txt", "r+", encoding='utf8') # Dosyayı açtık.
    liste = dosya.read().splitlines() # Dosyayı satır satır şeklinde listeye yazdırdık.
    dosya.close() # Dosyayıı kapattık.
    yeni_liste = [] # Geçici bir liste tanımladık.
    flag = 0  # Eğer silinmek istenen kitap bulunursa 1 yapılacak.
    for i in liste:  # Tüm kitapları aradık.
        if (i.split("\"")[1] == kitap_ismi):  # Aranan kitap bulunursa silme işlemi için flag i 1 e eşitledik.
            flag = 1
            print("| Kitap : " + i.split("\"")[1] + " | silindi.\n")
        else:
            yeni_liste.append(i)
    if(flag == 0):  # Aranan kitap bulunamadı bu yüzden dosyada değişiklik yapılmadı.
        print("Kitap bulunamadığı için silinemedi.")
    else:  # Aranan kitap bulundu ve silindi. o satır yeni listede bulunmayacağı için o satırı silmiş olarak dosyaya yeni kitap listesini kaydettik.
        dosya = open("kutuphane.txt", "w+", encoding="utf-8")

        for i in yeni_liste:
            dosya.write(i+str("\n"))
        dosya.close()

def baski_yukselt(kitap_ismi):
    dosya = open("kutuphane.txt", "r+", encoding='utf8')
    liste = dosya.read().splitlines()
    dosya.close()
    yeni_liste = []
    flag = 0
    for i in liste:
        if (i.split("\"")[1] == kitap_ismi):
            flag = 1
            baski_yeni=i.split("\"")
            baski_yeni[9]=str(int(baski_yeni[9])+1)
            baski_yeni="\"".join(baski_yeni)
            yeni_liste.append(baski_yeni)
        else:
            yeni_liste.append(i)
    if (flag == 1):
        dosya = open("kutuphane.txt", "w+", encoding="utf-8")

        for i in yeni_liste:
            dosya.write(i + str("\n"))
        dosya.close()
        return 1
    else:
        return 0

while True:
    print("""***********************************

    Kütüphane Programına Hoşgeldiniz.

    İşlemler;

    1. Kitapları Göster

    2. Kitap Sorgulama

    3. Kitap Ekle

    4. Kitap Sil 

    5. Baskı Yükselt

    Çıkmak için 'q' ya basın.
    ***********************************""")
    işlem = input("Yapacağınız İşlem : ")

    if (işlem == "q"):
        print("Program Sonlandırılıyor.....")
        print("Yine bekleriz....")
        break
    elif (işlem == "1"): # Tüm Kitapları Gösterme

        kitaplari_goster()  # Kitap Gösterme Fonksiyonu
        time.sleep(2)

    elif (işlem == "2"): # Kitap Sorgu
        isim = input("Hangi kitabı istiyorsunuz ? : ")
        print("Kitap Sorgulanıyor...")
        time.sleep(1)

        kitap_ara(isim)  # Kitap sorgulama fonksiyonuna gitti.
        time.sleep(2)

    elif (işlem == "3"): # Kitap Ekle
        isim = input("İsim: ")
        yazar = input("Yazar: ")
        yayinevi = input("Yayınevi: ")
        tur = input("Tür: ")
        while 1:  # Kullanıcı sayı girmesi gerektiği için sayı girene kadar input alındı.
            try:
                baski = int(input("Baskı: "))
            except ValueError:  # Sayı girmez ise tekrar sorç
                print("Lütfen sayı giriniz.")
                continue
            else:
                break


        print("Kitap ekleniyor....")
        time.sleep(1)

        kitap_ekle(isim,yazar,yayinevi,tur,baski)  # Kitap ekle fonksiyonu çağırıldı.
        print("Kitap Eklendi....")
        time.sleep(1)


    elif (işlem == "4"): # Kitap Silme
        isim = input("Hangi kitabı silmek istiyorsunuz ? : ")  # Kitap ismi kullanıcıdan alındı.

        cevap = input("Emin misiniz ? (E/H) : ")  # Silmeden önce tekrar emir beklendi.
        if (cevap == "E" or "e"):  # Eğer kullanıcı Evet der ise devam ediyoruzç
            print("Kitap Siliniyor...")
            time.sleep(1)
            kitap_sil(isim)  # Kitap Silme Fonksiyonu Çağırıldı.
            print("Kitap silindi....")
            time.sleep(1)


    elif (işlem == "5"): # Baskı Yukseltme Menüsü
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz ? : ")
        print("Baskı yükseltiliyor....")
        time.sleep(1)
        if(baski_yukselt(isim)):  # Baskı yükseltme fonsiyonu çağırıldı. Eğer fonksiyondan 1 dönerse Baskı başarıyle yükseltildi.
            print("Baskı yükseltildi....")
            time.sleep(1)
        else:
            print("Kitap Bulunamadığıı için baskı yükseltilemedi.")  # Eğer fonksiyondan 0 dönerse kitap bulunamadı.
            time.sleep(2)

    else: # Menüdeki işlemler dışında bir işlem yapılırsa bu kısıma girer.
        print("Geçersiz İşlem...")
        time.sleep(2)
        
