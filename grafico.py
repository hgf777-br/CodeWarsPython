import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as line

u = 0
d = 1

fig, ax = plt.subplots()
x = np.arange(-20, +20, 0.1)

# Curva Normal
# y = (1/d*math.sqrt(2*math.pi))*pow(math.e, (-(x-u)**2/2*(d**2)))

# y = pow(math.e, x)

y = x**5 - x**4 + x**3 - x**2 + x
ax.plot(x, y, 'g')

plt.show()
