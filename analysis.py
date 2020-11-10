# %%
import csv
from list_csv import list_csv

try_path = "/Users/renxmac/Desktop/lane 1-1.csv"
try_path = list_csv(try_path)

# %% Extract data from tpm csv file
for file_path in try_path:
    with open(file_path) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        total_column, x_list, y_list = [], [], []
        for column in reader:
            aoi = int(column[1])
            x_value = float(column[8])
            y_value = float(column[9])

            total_column.append(aoi)
            x_list.append(x_value)
            y_list.append(y_value)
# %%
