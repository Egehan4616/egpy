from decimal import Subnormal
import time
import os

surum = 3.0
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
        dosya = open("vars.txt", "a")
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
        nfn = input("dosya ismi")
        file = open(nfn,"w")
        file.write("eg[*]"+input("satır yaz =>")+"\n")
        file.close
    
    if sec == "write":
        print("write 'filename.txt'")
    
    if sec == "write file":
        wfn = input("dosya ismi")
        wfile = open(wfn,"a")
        wfile.write("eg[*] "+input("satır yaz =>")+"\n" )
        wfile.close
    
    

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