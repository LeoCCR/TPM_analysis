# %%
import csv
from list_csv import list_csv

try_path = "C:\\Users\\hwligroup\\Desktop\\lane 1-1.csv"
try_path = list_csv(try_path)

# %%
for file_path in try_path:
    with open(file_path) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for index, column_header in enumerate(header_row):
            print(index, column_header)

# %%
