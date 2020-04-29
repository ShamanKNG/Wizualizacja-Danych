import numpy as np
def fun(n):
    n=int(n)
    tab=np.arange(1,(n*n)+1)
    return tab
 
def fun1(n):
    n=int(n)
    for a in range (n):
        tab=np.arange(n*a+1,n*a+n+1)
        print(tab)
    

przyklad=fun(5)
print(przyklad)
print(przyklad.shape)
fun1(5)
fun1(2)
fun1(8)
