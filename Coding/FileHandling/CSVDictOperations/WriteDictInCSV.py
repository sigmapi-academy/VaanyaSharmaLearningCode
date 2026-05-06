import csv

#  List of dictionaries
students = [
    {'roll':1, 'name':'Shiv', 'marks':90},
    {'roll':2, 'name':'Ram', 'marks':94},
    {'roll':3, 'name':'Kartik', 'marks':88},
    {'roll':4, 'name':'Lakshmi', 'marks':92},
    {'roll':5, 'name':'Ganesh', 'marks':93},
]

# Field names (CSV columns)
fields = ['roll', 'name', 'marks']

# Writing to CSV.

with open("CSVFiles/students.csv", "w", newline='') as fo:
    writer = csv.DictWriter(fo, fieldnames=fields)
    
    writer.writeheader()    # Write column names 
    writer.writerows(students) # Writing data 
    
    