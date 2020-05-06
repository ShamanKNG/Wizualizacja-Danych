import numpy as np
a = np.arange(3)
b = np.arange(1.3,2.5,0.5)
print(a)
print(b)
c=a*b
print("mnożenie a*b:",c)
print("typ c:",c.dtype)
print("iloczyn macierzy a i b",a.dot(b))