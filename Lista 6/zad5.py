import numpy as np
def fun(n):
    wektor=np.arange(n, 0,-1)
    macierz=np.diag([n for a in range(n)])
    print(wektor)
    print(macierz)

fun(3)
fun(5)
fun(9)