import numpy as np
from decimal import Decimal

def f(x):
    z = str(x)
    y = Decimal(z)
    return np.sqrt(1+y)-1

target = 2.6e-08
target = 1e-15

print(f"{target} - {f(target)}")

