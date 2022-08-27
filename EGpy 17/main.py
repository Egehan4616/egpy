from decimal import Subnormal
import time
surum = 1.7
tarih = time.time()
lang = "tr"
page = 1
fonksiyonlar = ("oyun","tarih","sürüm","seçenekler","egpy terminal","help","lang","page+","page-" )
def func():
    global nmtf
    global nmd
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
        fonksiyonlar = ("set","name","show")
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

