# 1. Write a Python program to create a Student Management System using CSV files.
# The program should allow the user to:
# 	○ Add new student records
# 	○ Display all student records
# 	○ Search a student by roll number
# 	○ Update marks of a student
# 	○ Delete a student record
# 	○ Calculate total marks and percentage
# Handle exceptions such as invalid input, missing file, and incorrect roll number


# Create file with header if not exist.

def createFile():
    # write your code to create file 
    pass

# Add new student in the file
def add_student():
    # write your code 
    # open the file in append mode and add student 
    print('Student added successfully!')
    
# Display all students 
def display_students():
    # write your code
    # open the file in read mode and display all students 
    pass

# Search student. 
def search_student():
    roll = input('Enter Roll Number to search: ')
    # write your code
    pass

# Update student marks. 
def update_student():
    roll = input('Enter roll number to update: ')
    # write your code
    pass

# Delete student record
def delete_student():
    roll = input('Enter roll number to update: ')
    # write your code
    pass

# menu
def menu():
    
    
    while True:
        print('==========Student Management System==========')    
        print('1. Add student')
        print('2. Display all students' )
        print('3. Search student')
        print('4. Update Student')
        print('5. Delete Student')
        print('6. Create a file')
        print('0. Exit')
        
        choice = int(input('Enter your choice (0-5): '))
        
        match choice:
            case 1:
                add_student()
            case 2:
                display_students()
            case 3:
                search_student()
            case 4:
                update_student()
            case 5:
                delete_student()
            case 6:
                createFile() #to create a new file
            case 0:
                print('-'*50)
                print('Good Bye')
                break #terminate the infinite loop
            case _:
                print('Invalid choice!')
                
# main code
menu()
