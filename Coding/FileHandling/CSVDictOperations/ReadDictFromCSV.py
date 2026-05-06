import csv

with open("CSVFiles/students.csv", "r") as fo:
    reader = csv.DictReader(fo)
    
    for row in reader:
        print(row)