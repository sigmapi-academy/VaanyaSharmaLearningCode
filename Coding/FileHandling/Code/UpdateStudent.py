# consider the binary file student.dat storing the student details, which you created earlier
# programs. Write a program to update the records of the file student.dat, So that those who 
# have secured more than 81.0 get additional bonus marks of 2. 

import pickle

stu={}
found = False
with open('FileHandling/DataFiles/student.dat', "rb+") as fo:
    try:
        while True:
            rpos = fo.tell() # Store file pointer position before reading the record.
            stu = pickle.load(fo)
            
            if stu['marks'] > 81:
                stu['marks'] += 2 # Changes made in the record. Two bonus marks added.
                fo.seek(rpos)
                pickle.dump(stu, fo)
                found = True
    except EOFError:
        if found == False:
            print("Sorry, no matching records found.")
        else:
            print("Record(s) successfully updated.")
        