import numpy as np
b = np.arange(12)
print(b)
c=b.reshape((4,3))
print(c)
d=b.reshape((3,4))
e=b.reshape((2,6))
print(d,"\n")
print(e,"\n")
for a in c.flat:
   print(a)
print("\n")
for a in d.flat:
   print(a)
print("\n")
for a in e.flat:
   print(a)#są identyczne