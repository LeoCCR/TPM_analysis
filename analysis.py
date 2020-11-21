# %%
import csv
from list_csv import list_csv
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt

try_path = "/Users/renxmac/Desktop/lane 1-1.csv"
try_path = list_csv(try_path)
try_fit_ratio = 0.99
pixel_size = 71.5
xy_ratio_max = 1.15
xy_ratio_min = 0.85
try_corrcoef = 0.2

# %% Extract data from tpm csv file
aoi_x_frames, x_list, y_list = [], [], []

for file_path in try_path:
    with open(file_path) as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            aoi = int(row[1])
            x_value = float(row[8])
            y_value = float(row[9])

            aoi_x_frames.append(aoi)
            x_list.append(x_value)
            y_list.append(y_value)

# %% Reshape data array into #frames x #aoi.

num_aoi = aoi_x_frames[-1]
num_frame = int(len(aoi_x_frames)/num_aoi)

x_list = np.array(x_list, copy=False)
x_list = np.reshape(x_list, (num_frame, num_aoi))
y_list = np.array(y_list, copy=False)
y_list = np.reshape(y_list, (num_frame, num_aoi))

# %% Delete fitting ratio < criteria.

num_fit = np.count_nonzero(x_list, axis=0)
fit_ratios = np.true_divide(num_fit, num_frame)

column_to_del = [
    column for (column, fit_ratio) in enumerate(fit_ratios)
    if fit_ratio < try_fit_ratio
]

x_list = np.delete(x_list, column_to_del, axis=1)
y_list = np.delete(y_list, column_to_del, axis=1)
valid_num_aoi = len(x_list[0, :])

# %% replace 0 value with numpy nan veriable.

x_list[x_list == 0] = np.nan
y_list[y_list == 0] = np.nan

# Calculate BM x/y ratio.

bm_x = np.nanstd(x_list, axis=0)
bm_y = np.nanstd(y_list, axis=0)
bm_avr = bm_x/bm_y


# %%
column_fail_xy_ratio = [
    column for (column, bm) in enumerate(bm_avr)
    if bm < xy_ratio_min or bm > xy_ratio_max
]

corrcoefs = [
    abs(
        ma.corrcoef(
            ma.masked_invalid(x_list[:, aoi]),
            ma.masked_invalid(y_list[:, aoi])
        )[0, 1]
    )
    for aoi in range(valid_num_aoi)
]

column_fail_corrcoef = [
    column for (column, corrcoef) in enumerate(corrcoefs)
    if corrcoef > try_corrcoef
]

column_delete = sorted(
    list(
        set(column_fail_xy_ratio + column_fail_corrcoef)
    )
)

x_list = np.delete(x_list, column_delete, axis=1)
y_list = np.delete(y_list, column_delete, axis=1)

valid_num_aoi = len(x_list[0, :])
