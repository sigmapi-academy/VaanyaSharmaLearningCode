import csv

def append_student(record:dict):
    # Field names (CSV columns)
    fields = ['roll', 'name', 'marks']

    # Writing to CSV.
    try:
        with open("CSVFiles/students.csv", "a", newline='') as fo:
            writer = csv.DictWriter(fo, fieldnames=fields)
            writer.writerow(record) # Appended dictionary 
            print('Record appended successfully')
    except FileNotFoundError:
        print('File not found')
        

if __name__ == '__main__':
    di = dict()
    rn = int(input('Enter roll number: '))
    nm = input('Enter name of student: ')
    marks = int(input('Enter marks: '))
    di['roll']  = rn
    di['name'] = nm
    di['marks'] = marks
    append_student(di)
      
        