pi=3.142
def kira_kuboid(tinggi,panjang,lebar):
     isipadu_kuboid=h*l*w
     return isipadu_kuboid

def kuboid():
     h = float(input("Masukkan tinggi:"))
     l = float(input("Masukkan panjang:"))
     w = int(input("Masukkan lebar:"))
     print("Isi padu kuboid=", kira_kuboid(tinggi,panjang,lebar))

def kira_silinder(pi , r, h):
     isipadu_silinder=pi*r*r*h
     return isipadu_silinder

def silinder():
     r = float(input("Masukkan jejari:"))
     h = float(input("Masukkan tinggi:"))
     print("Isi padu silinder=", kira_silinder(pi, r, h))

def kira_kon(pi , r, h):
     isipadu_kon=(1/3)*pi*r*r*h
     return isipadu_kon

def kon():
     r = float(input("Masukkan jejari:"))
     h = float(input("Masukkan tinggi:"))
     print("Isi padu kon=", kira_kon(pi, r, h))

def kira_sfera(pi, r):
     isipadu_sfera = (4/3) * pi * r ** 3
     return isipadu_sfera

def sfera():
     r = float(input("Masukkan jejari:"))
     print("Isi padu sfera=", kira_sfera(pi, r))

ulang = True

while(ulang):
     print("***********************************\n       Menu Mengira Isi Padu       \n***********************************")
     print("1. Kuboid\n2. Silinder\n3. Kon\n4. Sfera\n5.Tamat program***********************************")

     pilih=int(input("Sila masukkan pilihan anda:"))

     if(pilih==1):
          kuboid()
     elif(pilih==2):
          silinder()
     elif(pilih==3):
          kon()
     elif(pilih==4):
          sfera()
     elif(pilih==5):
          ulang=False
          print("Bye Bye")
          exit
     else:
          print("Pilihan tiada dalam senarai")
          print("")
          
          
          

     
    
