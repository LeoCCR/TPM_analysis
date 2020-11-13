import numpy as np
import scipy as sp
from random import randrange

x = np.array([float(randrange(start=1, stop=5)) for _ in range(10)])
y = np.array([float(randrange(start=1, stop=5)) for _ in range(10)])
x[x == 1] = np.nan
y[y == 1] = np.nan

print(x)
print(y)

print(abs(np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y))[0, 1]))
