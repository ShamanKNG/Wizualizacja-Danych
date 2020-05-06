import numpy as np
a= np.arange(9).reshape(3,3)
b= np.arange(16).reshape(4,4)
print(a)
print(b)
print("minimum rzędów a ", a.min(axis=1))
print("minimum rzędów b ", b.min(axis=1))
print("minimum kolumn a ", a.min(axis=0))
print("minimum kolumn b ", b.min(axis=0))