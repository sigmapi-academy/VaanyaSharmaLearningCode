import os
import csv
os.system('cls')


def main(): 

    while True: 

        print("Welcome to the Student Management System!") 

        print("Would you like to...") 

        print("A. Add New Student") 

        print("B. Display all students") 

        print("C.Search For a Student") 

        print("D. Update Student Marks") 

        print("E. Delete Student Record") 

        print("F. Calculate total Marks and Percentage") 

        print("G. Exit Menu") 

        ans = input("What is your choice?") 

        if ans.lower() == 'a': 

            AddStudent() 

        elif ans.lower() == 'b': 

            DisplayAllRecords() 

        elif ans.lower() == 'c': 

            SearchForStudent() 

        elif ans.lower() == 'd': 

            UpdateMarks() 

        elif ans.lower() == 'e': 

            DeleteStudent() 

        elif ans.lower() == 'f': 

            CalcTotalMarks() 

        elif ans.lower() == 'g': 

            print("Goodbye!") 

            break 

        else: 

            print("Please enter a valid input.") 

  
def AddStudent(): 

    Name = input("Enter the name of the student: ") 

    Rollnumber = int(input("Enter the roll number of the student: "))

    Marks = int(input("Enter the marks of the student: ")) 

    student = [Rollnumber, Name, Marks]

    with open(file, 'a', newline='') as fo:
        stuwriter = csv.writer(fo)
        stuwriter.writerow(student)

def DisplayAllRecords(): 
    print("Here are all the students: ")
    
    with open(file, 'r', newline='') as fo:
        stureader = csv.reader(fo)
        
        for rec in stureader:
            print(rec)
            print('-' * 67)

        
def SearchForStudent(): 

    pid = input("Enter the Roll Number you want to search for: ")

    found = False 

    with open(file, 'r', newline='') as fo:
        stureader = csv.reader(fo)
        
        for rec in stureader: 
            if rec[0] == pid: 

                print("Student found!") 

                print(rec) 

                found = True 

    if not found: 

        print("Sorry, the student was not found.") 

  
def UpdateMarks(): 

    pid = input("Enter the ID which you want to update: ")
    nmarks = input("Enter the updated marks: ")

    recs = []

    with open(file, 'r', newline='') as fo:
        stureader = csv.reader(fo)

        for rec in stureader: 

            if rec[0] == pid: 

                print("Student found!") 
                print(rec)

                ans = input("Is this the student whose ID you want to update?(Answer 'y' for yes and 'n' for no.) \n")

                if ans.lower() == 'y':
                    rec[2] = nmarks

                elif ans.lower() == 'n':
                    print("Sorry, the student was not found")

                else:
                    print("Please answer with 'y' or 'n'. ")

            recs.append(rec)

    with open(file, 'w', newline='') as fo:
        stuwriter = csv.writer(fo)
        stuwriter.writerows(recs)

                        
def DeleteStudent(): 

    pid = input("Enter the ID which you want to delete: ") 

    recs = []

    with open(file, 'r', newline='') as fo:
        stureader = csv.reader(fo)

        for rec in stureader: 

            if rec[0] == pid: 

                print("Student found!") 
                print(rec)

                ans = input("Is this the student whose ID you want to delete?(Answer 'y' for yes and 'n' for no.) \n")

                if ans.lower() == 'y':
                    continue

                elif ans.lower() == 'n':
                    print("Sorry, the student was not found")

                else:
                    print("Please answer with 'y' or 'n'. ")

            recs.append(rec)

    with open(file, 'w', newline='') as fo:
        stuwriter = csv.writer(fo)
        stuwriter.writerows(recs)

    print("Record Deleted!")

def CalcTotalMarks(): 

    count = 0 
    num = 0

    with open(file, 'r', newline='') as fo:
        stureader = csv.reader(fo)

        for rec in stureader: 
            n = int(rec[2]) 

            count += n
            num += 1

    print("The total marks are: ", count) 

    if num != 0:
        print("The average marks are:", count / num)
    else:
        print("No records found.") 

  #main code starts here
file = input("Enter the filename you want to use. It should be a CSV file. \n")
main()

