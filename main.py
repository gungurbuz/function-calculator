import math
import time
while True:
 def faktoryel():
  print ("sonuç:")
  print (math.factorial(math.fabs(sayi1)))

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
 print ("7= faktöryel")

 secim = input("işlemini seç: ")
 #asking the user to choose an operation




 if secim == "1":
  sayi1 = int(input("sayı1 gir: "))
  sayi2 = int(input("sayı2 gir: "))
  #taking the numbers as an input
  print("hesaplanıyor")
  time.sleep(3)
  toplama()
  time.sleep(3.5)
 elif secim == "2":
  sayi1 = int(input("sayı1 gir: "))
  sayi2 = int(input("sayı2 gir: "))
  print("hesaplanıyor")
  time.sleep(3)
  cikarma()
  time.sleep(3.5)
 elif secim == "3":
  sayi1 = int(input("sayı1 gir: "))
  sayi2 = int(input("sayı2 gir: "))
  print("hesaplanıyor")
  time.sleep(3)
  carpma()
  time.sleep(3.5)
 elif secim == "4":
  sayi1 = int(input("sayı1 gir: "))
  sayi2 = int(input("sayı2 gir: ")) 
  print("hesaplanıyor")
  time.sleep(3)
  bolme()
  time.sleep(3.5)
 elif secim == "5":
  sayi1 = int(input("sayı1 gir: "))
  sayi2 = int(input("sayı2 gir: "))
  print("hesaplanıyor")
  time.sleep(3)
  uslusayi()
  time.sleep(3.5)
 elif secim == "6":
  sayi1 = int(input("sayı1 gir: "))
  print("hesaplanıyor")
  time.sleep(3)
  karekok()
  time.sleep(3.5)
 elif secim == "7":
  sayi1 = int(input("sayı1 gir: "))
  print("hesaplanıyor")
  time.sleep(3)
  faktoryel()
  time.sleep(3.5)
  #the if elif function to execute when the 
  #representing number is chosen
 cevap = input("yeniden çalıştırmak istiyor musunuz?(E/H): ")
 if cevap == "E" or cevap == "e":
   print ("tamam ozaman")

 elif cevap == "H" or cevap == "h":
  print ("tamam ozaman baybay")
  break

 else:
  print ("malsın sen e veya h yaz")
  break

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