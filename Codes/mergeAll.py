import os
import glob
import pandas as pd

# Path to the folder containing CSV files
folder_path = './'

# Get a list of all CSV files in the folder
csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

print(len(csv_files))

# Initialize total row count
total_rows = 0

# Iterate through each CSV file and count rows
for csv_file in csv_files:
    print(csv_file)
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    # Count the number of rows in the DataFrame and add to total row count
    print(len(df))
    total_rows += len(df)

print("Total number of rows in all CSV files:", total_rows)

import glob

interesting_files = glob.glob("*.csv") 

header_saved = False
with open('outputAll.csv','wb') as fout:
    for filename in interesting_files:
        with open(filename, 'rb') as fin:
            header = next(fin)
            if not header_saved:
                fout.write(header)
                header_saved = True
            for line in fin:
                fout.write(line)