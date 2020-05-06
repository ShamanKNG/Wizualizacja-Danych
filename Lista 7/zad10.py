import numpy as np
b = np.arange(81).reshape(9,9)
print(b)
#c=b.reshape((8,8)) musi miec 81 miejsc tak samo jak macierz początkowa
c=b.reshape((27,3))#81
d=b.reshape((81,1))#81
print(c)
print(d)
e= b.ravel()
print(e)
f=b.T
print(f)
