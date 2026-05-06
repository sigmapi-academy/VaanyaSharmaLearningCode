import os
os.system('cls')
numOfStudents = 10
start = 1
count95 = 0
count90 = 0
while start <= numOfStudents :
    print('Enter marks for student:',start)
    English = int(input('Enter marks of English: '))
    Maths = int(input('Enter marks of Maths: '))
    Science = int(input('Enter marks of Science: '))
    
    agg = (English + Maths + Science)/3
    print(f'Aggregate: {agg:.2f}')
    if agg >= 95:
        count95 += 1
    elif agg >= 90:
        count90 += 1
    
    start += 1

print('Number of students aggregate >= 95 is:',count95)
print('Number of students aggregate >= 90 is:',count90)
