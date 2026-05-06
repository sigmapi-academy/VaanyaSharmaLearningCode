import csv

def delete_record(rollNumb:int):
    data = []
    found = False

    try:
        with open("CSVFiles/students.csv", "r") as fo:
            reader = csv.DictReader(fo)
            for row in reader:
                if int(row['roll']) != rollNumb:
                    data.append(row) # Keep the record 
                else:
                    found = True # mark found
    except FileNotFoundError:
        print('File not found')        
    
    if found:
        print('Record Deleted successfully')
        try:
            with open('CSVFiles/students.csv', 'w', newline='') as fo:
                fields = ['roll', 'name', 'marks']
                writer = csv.DictWriter(fo, fieldnames=fields)
                writer.writeheader()
                writer.writerows(data)
        except FileNotFoundError:
            print('File not found')
    else:
            print(f'Roll number {rollNumb} is not present')
if __name__ == '__main__':
    rollNumb = int(input("Enter roll number to delete the record of student: "))
    delete_record(rollNumb)