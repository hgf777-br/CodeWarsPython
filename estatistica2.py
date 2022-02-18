import statistics as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

x = [1.3,3.4,5.1,6.8,8.0]
y = [2.0,5.2,3.8,6.1,5.8]

x1 = np.arange(0.1, 1, 0.1)
y1 = [0.459, 0.828, 1.006, 1.15, 1.354, 1.261, 1.157, 0.834, 0.511]

print(np.corrcoef(x,y))
print("-" * 40)

def regressao_simples(x,y):
  sxy = sum([x * y for x, y in zip(x, y)])
  sx = sum(x)
  sy = sum(y)
  sx2 = sum([x**2 for x in x])
  s2x = sum(x)**2
  n = len(x)
  b = (n*sxy - sx*sy) / (n*sx2 - s2x)
  a = (sy - b*sx) / n
  return a, b

def minimos_quadrados(x,y):
  b = np.corrcoef(x,y)[0,1]*np.std(y)/np.std(x)
  a = np.mean(y) - b*np.mean(x)
  return (a, b)

def reg_Linear(a,b,x):
  return a + b*x

print(regressao_simples(x,y))
