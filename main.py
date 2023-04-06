import csv

import os




data = [
    [0],
    ["John Doe", 25, "Male"],
    ["Jane Smith", 30, "Femmmale"],
    ["Bob Johnson", 45, "Male"],
]

def writer(data):
    file_name = "encrypted.csv"
    with open(file_name, mode="w", newline="") as csv_file:

    # Create a CSV writer object
        writer = csv.writer(csv_file)

    # Write the data to the CSV file
        for row in data:
            writer.writerow(row)
    
writer(data)
filename = "encrypted.csv"
os.system(f'start excel {filename}')