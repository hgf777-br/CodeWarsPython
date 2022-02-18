import statistics as st
import numpy as np
import matplotlib.pyplot as plt

x = [6,5,9,10,3,4,8,7,6,2]
y = [7,6,10,9,2,3,9,5,6,3]

print(len(x), len(y))
print(st.mean(x), st.mean(y))
print(st.pstdev(x), st.pstdev(y))

N = st.NormalDist(100,10)

print(list(map(round, N.quantiles())))

print('-' * 40)

print(np.mean(x), np.mean(y))
print(np.median(x), np.median(y))
print(np.std(x), np.std(y))
print(np.corrcoef(x,y))
print(np.correlate(x,y))

plt.plot(x,y, 'bo')

plt.show()
