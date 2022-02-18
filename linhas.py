import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as line

fig, ax = plt.subplots()
x = np.arange(-math.pi,math.pi,0.1)
y = np.sin(x)
y2 = np.cos(x)
y3 = 5 + 2*x
print(x)
print(y)
#plt.axes(polar=True)
plt.xlim(-4, 4)
plt.ylim(-4, 4)
ax.plot(x,y,'g')
ax.plot(x,y2,'r')
ax.plot(x,y3,'b')
#ax.plot([0,2],[0,2])

#fig.add_artist(line.Line2D([0,2], [0,2]))

plt.show()
