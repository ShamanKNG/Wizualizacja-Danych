import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 31, 0.1)
plt.plot(x,np.sin(-x),"orange", label='sin(x)')
plt.plot(x,np.sin(x)+2,"blue", label='sin(x)')
plt.axis([1, 31, -1.5, 3.5])
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title("Sinus i Sinus")
plt.legend()
plt.grid()

plt.show()