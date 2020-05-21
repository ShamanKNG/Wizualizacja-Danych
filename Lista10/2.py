import matplotlib.pyplot as plt
import numpy as np
x = [1/x for x in range(1,21)]


plt.plot(x,"g>--", label='f(x)=1/x')
plt.axis([0, 20, 0, 1])
plt.xlabel('x')
plt.ylabel('f(x)')

plt.title("Funkcja")
plt.legend()

plt.show()