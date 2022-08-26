from decimal import Subnormal
import time
surum = 1.0
tarih = time.time()
lang = "tr"
fonksiyonlar = ("oyun","tarih","sürüm","seçenekler","egpy terminal","help","lang" )



print("hello world !!")
time.sleep(3)
def func():
    
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
        print("=>","bu uygulama egehan kahraman tarfından asistan olarak geliştirilimiştir şu anki sürümü",surum,"dür daha fazlası için help.txt dosyasını çaıltırın",fonksiyonlar)

   # if sec != fonksiyonlar:
   #    print("kod satırında hata var !! yazım hatası")
   #    print("şuradan seçin veya kontrol edin", fonksiyonlar) 
   # işe yaramadı daha sonra
    
print("hoşgeldiniz burdan bir şeyler seçebilirsniz")
print(fonksiyonlar)          
while True:  
    func()

