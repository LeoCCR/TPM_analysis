# %%
import csv
from numpy.core.fromnumeric import reshape

from numpy.lib.function_base import copy
from list_csv import list_csv
import numpy as np

try_path = "/Users/renxmac/Desktop/lane 1-1.csv"
try_path = list_csv(try_path)

# %% Extract data from tpm csv file
total_column, x_list, y_list = [], [], []

for file_path in try_path:
    with open(file_path) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for column in reader:
            aoi = int(column[1])
            x_value = float(column[8])
            y_value = float(column[9])

            total_column.append(aoi)
            x_list.append(x_value)
            y_list.append(y_value)
# %%
num_aoi = total_column[-1]
num_frame = int(len(total_column)/num_aoi)
x_list = np.array(x_list, copy=False)
x_list = np.reshape(x_list, (num_aoi, num_frame))
y_list = np.array(y_list, copy=False)
y_list = np.reshape(y_list, (num_aoi, num_frame))

# %%
