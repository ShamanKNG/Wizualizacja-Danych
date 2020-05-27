import matplotlib.pyplot as plt
import numpy as np
import random

fig = plt.figure()
AX = plt.subplot(121, projection="3d")

X = np.arange(1 , 100 , 5 )
Y= np.arange(1 , 80 , 4 )
Z= np.arange(1 , 21 , 1 )
AX.scatter(X, Y, Z, color="red", marker="X")

r=5
ax = plt.subplot(122, projection="3d")
x = np.random.rand(r)
y = np.random.rand(r)
z = np.random.rand(r)
ax.plot(x, y, z, color="b", marker="*")
plt.show()