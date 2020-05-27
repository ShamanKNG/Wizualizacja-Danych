import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import random

ax = plt.subplot(111, projection="3d")

kolory = ["r", "g", "m", "olive", "y"]
znacznik = ["x", "X", "D", "8", "d"]
a = 10
for i in range(5):
    x = np.random.rand(a)
    y = np.random.rand(a)
    z = np.random.rand(a)
    ax.scatter(x, y, z, c=kolory[i], marker=znacznik[i])

plt.show()