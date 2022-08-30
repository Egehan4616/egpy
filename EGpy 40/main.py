from decimal import Subnormal
import shutil
import time
import os

surum = 5.0
tarih = time.time()
lang = "tr"
page = 1
nmd = "egpy"
fonksiyonlar = ("oyun","tarih","sürüm","seçenekler","egpy terminal","help","lang","page+","page-" )
def clear():
    os.system('cls')
def func():
    global nmtf
    global nmd
    global lang
    global fonksiyonlar
    sec=input("eg=>")
    
    if sec == "sürüm":
        print("=>",surum)
    
    if sec == "oyun":
        print("=>","bu klasör içersinden games dizine geçin ordaki oyun klasölerinde var")
    
    if sec == "tarih":
        print("=>",tarih)

    if sec == "seçenekler":
        print("=>",fonksiyonlar)

    if sec == "egpy terminal":
        print("=>","bu klasör içerisinden term.py dosyasını açın ")

    if sec == "lang":
        print("=>","şu anki dil",lang)
    
    if sec == "help":
        print("=>") #,"bu uygulama egehan kahraman tarfından asistan olarak geliştirilimiştir şu anki sürümü",surum,"dür daha fazlası için help.txt dosyasını çaıltırın",fonksiyonlar)
        helpd = open("help.txt","r")
        print(helpd.read())
    
    if sec == "page+":
        fonksiyonlar = ("set","name","show","var","lang","change","uyu","open","file")
        print(fonksiyonlar)

    if sec == "page-":
        fonksiyonlar = ("oyun","tarih","sürüm","seçenekler","egpy terminal","help","lang","page+","page-" )
        print(fonksiyonlar)
    
    if sec == "set Name":
        nmd = input("set Name =>")
        nmtf = nmd
        print("ismim artık =>",nmd)

    if sec == "name":
            print("ismim  =>",nmd)

    if sec == "show Options":
        shwo = open("func.txt","r")
        print(shwo.read())
    
    if sec == "new var":
        #global dosya
        #nvw = input("new var =>")
        dosya = open("data\vars\vars.txt", "a")
        dosya.write(","+input("new var =>")+"\n")
        dosya.close
    
    if sec == "var":
        print("new var 'var name'")

    if sec == "show":
        print("show 'options")
    
    if sec == "show Vars":
        shwv = open("vars.txt","r")
        print(shwv.read())
    
    if sec == "set change lang":
        print("set change lang 'lang name'")
    
    if sec == "set change lang 'tr'":
        lang= "tr"
        print("işlem tamamdır")
    
    if sec == "set change lang 'uk'":
        lang= "uk"
        print("succsesfull")
    if sec == "uyu":
        uyukadar=int(input("uyu => " ))
        time.sleep(uyukadar)
        print("uyuma tamamlandı")

    if sec == "open":
        print("open file 'file.txt'")

    if sec == "open file":
        fln =input("file name =>")
        ofl = open(fln,"r")
        print("dosya okunuyor")
        print(ofl.read())
    
    if sec == "clear":
        clear()
    
    if sec == "new file":
        global yeni_file_satir
        global yeni_file_ismi
        global yeni_file_dosya
        global i
        i = 0
        yeni_file_ismi = input("dosyanın ismi =>")
        yeni_file_dosya = open('data/files/'+yeni_file_ismi,"w")
        yeni_file_satir = int(input("satir sayisi =>"))
        while i < yeni_file_satir:
            yeni_file_dosya = open('data/files/'+yeni_file_ismi,"a")
            yeni_file_dosya.write(input("satir =>")+"\n")
            i += 1
            yeni_file_dosya.close
    
    if sec == "write":
        print("write 'filename.txt'")
    
    if sec == "write file":
        global efile_satir
        global efile_ismi
        global efile_dosya
        global inytt
        inytt = 0
        efile_ismi = input("doysa ismi =>")
        efile_dosya = open('data/files/'+efile_ismi,"w")
        efile_satir = int(input("satir sayisi =>"))
        while inytt < efile_satir:
            efile_dosya = open('data/files/'+efile_ismi,"a")
            efile_dosya.write(input("satir =>")+"\n")
            inytt += 1
            efile_dosya.close
    
    if sec == "open game":
        oynd= input("açılacak oyunun bağlantısını yazın =>")
        os.system(oynd)
        print("oyun açıldı")
        func()

    if sec == "open game cr":
        os.system("games\crafthan\crafthan.py")
        print("oyun açıldı")

    if sec == "copy game":
        oyun_ismi = input("oyunun ismi =>")
        oyun_kodlari = input("oyun kodları hangi dizinde =>")
        oyun_copy = shutil.copy(oyun_kodlari,"games")
        os.rename(oyun_copy,oyun_ismi)
        print("işlen bitti")
   
    if sec == "new game":
        global yeni_oyun_satir
        global yeni_oyun_ismi
        global yeni_oyun_dosya
        global iny
        iny = 0
        yeni_oyun_ismi = input("oyunun ismi =>")
        yeni_oyun_dosya = open('data/files/'+yeni_oyun_ismi,"w")
        yeni_oyun_satir = int(input("satir sayisi =>"))
        while iny < yeni_oyun_satir:
            yeni_oyun_dosya = open('data/files/'+yeni_oyun_ismi,"a")
            yeni_oyun_dosya.write(input("satir =>")+"\n")
            iny += 1
            yeni_oyun_dosya.close
    
    if sec == "edit file":
        global yeni_efile_satir
        global yeni_efile_ismi
        global yeni_efile_dosya
        global inyt
        inyt = 0
        yeni_efile_ismi = input("doysa ismi =>")
        yeni_efile_dosya = open('data/files/'+yeni_efile_ismi,"w")
        yeni_efile_satir = int(input("satir sayisi =>"))
        while inyt < yeni_efile_satir:
            yeni_efile_dosya = open('data/files/'+yeni_efile_ismi,"a")
            yeni_efile_dosya.write(input("satir =>")+"\n")
            inyt += 1
            yeni_efile_dosya.close

    if sec == "komutlar":
        komut_dosyasi = open("command.txt","r")
        print("dosya okunuyor")
        print(komut_dosyasi.read())
        komut_dosyasi.close

    if sec == "write file with 'egpy'":
        global wefile_satir
        global wefile_ismi
        global wefile_dosya
        global inyttw
        inyttw = 0
        wefile_ismi = input("doysa ismi =>")
        wefile_dosya = open('data/files/'+wefile_ismi,"w")
        wefile_satir = int(input("satir sayisi =>"))
        while inyttw < wefile_satir:
            wefile_dosya = open('data/files/'+wefile_ismi,"a")
            wefile_dosya.write("eg[*]"+input("satir =>")+"\n")
            inyttw += 1
            wefile_dosya.close
            

   #if sec == "break":
   #        print ("işlem bitti")
    #        func()
    #    else:
   # if sec != fonksiyonlar:
   #    print("kod satırında hata var !! yazım hatası")
   #    print("şuradan seçin veya kontrol edin", fonksiyonlar) 
   # işe yaramadı daha sonra


print("hello world !!")
time.sleep(3)  
print("hoşgeldiniz burdan bir şeyler seçebilirsniz")
print(fonksiyonlar)          
while True:  
    func()