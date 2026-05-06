# Write a program to get student data (roll number, name and marks) from user
# and write onto a binary file. The program should be able to get data from 
# the user and write onto the file as long as the user wants.

import pickle

stu = {}

filename = input('Enter file name: ')
with open("FileHandling/DataFiles/"+filename+".dat", "ab") as fo:
    ans = 'y'
    count = 0
    while ans in ('y', 'Y'):
        rolln = int(input('Enter roll number: '))
        name = input('Enter name: ')
        marks = float(input('Enter marks: '))
        stu['Roll number'] = rolln
        stu['Name'] = name
        stu['marks'] = marks
        pickle.dump(stu, fo)
        count += 1
        ans = input('Want to enter more records(Y/N)... ')
    print(count,'records dumped into the file.')
    