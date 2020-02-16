import math
import time
def uslusayi ():
  print ("sonuç:")
  print (sayi1 ** sayi2)

def toplama ():
  print ("sonuç:")
  print (sayi1 + sayi2)
 #addition

def carpma ():
  print ("sonuç:")
  print (sayi1 * sayi2)
	#multiplication

def bolme ():
  print ("sonuç:")
  print (sayi1 / sayi2)
	#division

def cikarma ():
  print ("sonuç:")
  print (sayi1 - sayi2)
	#subtraction

def karekok ():
  print ("sonuç:")
  print (math.sqrt(sayi1))
  #square root

print ("işlem seç")
print ("1= toplama")
print ("2= çıkarma")
print ("3= çarpma")
print ("4= bölme")
print ("5= üslü sayı ** sayı1 taban, sayı2 üs olacaktır **")
print ("6= karekök ** sadece sayı1 kullanılacaktır **")

secim = input("işlemini seç: ")
#asking the user to choose an operation




if secim == "1":
  sayi1 = int(input("sayı1 gir: "))
  sayi2 = int(input("sayı2 gir: "))
  #taking the numbers as an input
  print("hesaplanıyor")
  time.sleep(3)
  toplama()
elif secim == "2":
  sayi1 = int(input("sayı1 gir: "))
  sayi2 = int(input("sayı2 gir: "))
  print("hesaplanıyor")
  time.sleep(3)
  cikarma()
elif secim == "3":
  sayi1 = int(input("sayı1 gir: "))
  sayi2 = int(input("sayı2 gir: "))
  print("hesaplanıyor")
  time.sleep(3)
  carpma()
elif secim == "4":
  sayi1 = int(input("sayı1 gir: "))
  sayi2 = int(input("sayı2 gir: ")) 
  print("hesaplanıyor")
  time.sleep(3)
  bolme()
elif secim == "5":
  sayi1 = int(input("sayı1 gir: "))
  sayi2 = int(input("sayı2 gir: "))
  print("hesaplanıyor")
  time.sleep(3)
  uslusayi()
elif secim == "6":
  sayi1 = int(input("sayı1 gir: "))
  print("hesaplanıyor")
  time.sleep(3)
  karekok()
#the if elif function to execute when the 
#representing number is chosen


#print (".")
#time.sleep(0.2)
#print ("..")
#time.sleep(0.2)
#print ("...")
#time.sleep(0.2)
#print ("....")
#time.sleep(0.2)
#print (".....")
#time.sleep(0.2)
#print ("......")
#time.sleep(0.2)
#print (".......")
#time.sleep(0.2)
#print ("........")
#time.sleep(0.2)
#print (".........")
#time.sleep(0.2)
#print ("..........")
#ill try to make this work later