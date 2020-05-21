import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 31, 0.1)
plt.plot(x,np.sin(x),"b", label='sin(x)')
plt.plot(x,np.cos(x),"r", label='cos(x)')
plt.axis([1, 31, -2, 2])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("Sinus i Cosinus")
plt.legend()
plt.grid()

plt.show()