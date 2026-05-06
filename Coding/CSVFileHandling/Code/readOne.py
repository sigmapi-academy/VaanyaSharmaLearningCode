import csv

file_name = input("Enter your file name: ")

with open("CSVFileHandling/CSVFiles/"+file_name+".csv", "r") as fh:
    csvrecords = csv.reader(fh)
    for rec in csvrecords:
        print(rec)