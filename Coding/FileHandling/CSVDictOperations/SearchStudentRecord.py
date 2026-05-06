import csv

with open("CSVFiles/students.csv", "r") as fo:
    reader = csv.DictReader(fo)
    rollNumb = int(input('Enter roll number to search: '))
    for row in reader:
        if int(row['roll']) == rollNumb:
            print(row)
            break
    else:
        print(f'Roll number {rollNumb} is not present')