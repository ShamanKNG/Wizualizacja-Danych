import random
macierz=[[random.randint(0,11) for n in range(4)]for n in range(4) ]
lista=[macierz[n][m]for n in range(4) for m in range(4)if n==m]
print(macierz)
print(lista)
