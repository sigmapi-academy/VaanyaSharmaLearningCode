import csv

# Write a program to create a CSV file to store student data (The roll number, Name, Marks)
# Obtain data from the user and write 5 records into the file. 

fileName = input("Enter your csv file name: ")
with open("CSVFileHandling/CSVFiles/"+fileName+".csv", "a", newline='') as fo:
    num_of_records = 5
    li=[]
    stu_writer = csv.writer(fo)
    stu_writer.writerow(['Roll_num','Name', 'Marks'])
    for i in range(num_of_records):
        roll_num = int(input("Enter the roll number: "))
        name = input("Enter name of the student: ")
        marks = float(input("Enter the average marks: "))
        li.append([roll_num, name, marks])
    stu_writer.writerows(li)
    
    
        
    