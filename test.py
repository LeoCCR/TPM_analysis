# %%
import numpy as np
import numpy.ma as ma
from random import randrange

x = np.array([float(randrange(1, 5)) for _ in range(10)])
y = np.array([float(randrange(1, 5)) for _ in range(10)])
# %%
x[x == 1] = np.nan
y[y == 1] = np.nan

print(x)
print(y)

print(abs(np.ma.corrcoef(np.ma.masked_invalid(x), np.ma.masked_invalid(y))[0, 1]))

# %%
x = ma.masked_equal(x, 1)
ma.count(x)
np.sum(x)
np.average(x)

# %%
