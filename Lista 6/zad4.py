import numpy as np
def fun(a,b):
    tab=np.logspace(1,b,base=a,dtype=int,num=b)
    return tab

    

print(fun(2,4))
print(fun(3,6))