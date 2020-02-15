sayi1 = int(input("sayi1 gir: "))
sayi2 = int(input("sayi2 gir: "))
#taking the numbers as an input

def toplama ():
 print ("___________________")
 print ("sonuç:")
 print (sayi1 + sayi2)
 #addition

def carpma ():
  print("___________________")
  print ("sonuç:")
  print (sayi1 * sayi2)
	#multiplication

def bolme ():
  print("___________________")
  print ("sonuç:")
  print (sayi1 / sayi2)
	#division

def cikarma ():
  print("___________________")
  print ("sonuç:")
  print (sayi1 - sayi2)
	#subtraction



print("___________________")
print ("işlem seç")
print ("1= toplama")
print ("2= çıkarma")
print ("3= çarpma")
print ("4= bölme")

secim = input("işlemini seç: ")
#asking the user to choose an operation

if secim == "1":
  toplama()
elif secim == "2":
  cikarma()
elif secim == "3":
  carpma()
elif secim == "4":
  bolme()
#the if elif function to execute when the 
#representing number is chosen