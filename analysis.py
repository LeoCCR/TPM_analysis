# %%
import csv

from list_csv import list_csv
import numpy as np
import numpy.ma as ma
from scipy.stats import pearsonr

try_path = "/Users/renxmac/Desktop/lane 1-1.csv"
try_path = list_csv(try_path)
try_fit_ratio = 0.99
pixel_size = 71.5
xy_ratio_max = 1.15
xy_ratio_min = 0.85


# %% Extract data from tpm csv file
total_column, x_list, y_list = [], [], []

for file_path in try_path:
    with open(file_path) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            aoi = int(row[1])
            x_value = float(row[8])
            y_value = float(row[9])

            total_column.append(aoi)
            x_list.append(x_value)
            y_list.append(y_value)
# %% Row = Aoi
num_aoi = total_column[-1]
num_frame = int(len(total_column)/num_aoi)

x_list = np.array(x_list, copy=False)
x_list = np.reshape(x_list, (num_frame, num_aoi))
y_list = np.array(y_list, copy=False)
y_list = np.reshape(y_list, (num_frame, num_aoi))

x_list = ma.masked_equal(x_list, 0)
y_list = ma.masked_equal(y_list, 0)

# %%
num_fit = ma.count(x_list, axis=0)
fit_ratios = np.true_divide(num_fit, num_frame)
# %%
column_to_del = [
    column for (column, fit_ratio) in enumerate(fit_ratios)
    if fit_ratio < try_fit_ratio
    ]

# %%
x_list = np.delete(x_list, column_to_del, axis=1)
y_list = np.delete(y_list, column_to_del, axis=1)
# %%

# %%
valid_num_aoi = len(x_list[0, :])
bm_x = [ma.std(x_list[:, aoi]) for aoi in range(valid_num_aoi)]
bm_y = [ma.std(y_list[:, aoi]) for aoi in range(valid_num_aoi)]
bm_avr = np.array(bm_x)/np.array(bm_y)

# corrcoef = [
#    np.ma.corrcoef(x_list[:, aoi], y_list[:, aoi])
#    for aoi in range(valid_num_aoi)
#    ]

# %%
# print(corrcoef)
