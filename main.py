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

print ("işlem seç")
print ("1= toplama")
print ("2= çıkarma")
print ("3= çarpma")
print ("4= bölme")
print ("5= üslü sayı **sayı1 taban, sayı2 üs olacaktır**")

secim = input("işlemini seç: ")
#asking the user to choose an operation

sayi1 = int(input("sayı1 gir: "))
sayi2 = int(input("sayı2 gir: "))
#taking the numbers as an input

if secim == "1":
  toplama()
elif secim == "2":
  cikarma()
elif secim == "3":
  carpma()
elif secim == "4":
  bolme()
elif secim == "5":
  uslusayi()

#the if elif function to execute when the 
#representing number is chosen