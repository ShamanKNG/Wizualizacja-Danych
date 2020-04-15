import sys
lista=[n for n in range(1,100) if n%4==0]
f=open("zad1.txt","a+")
f.write(str(lista))
f.close()