
# Write a program to enter names of employees and their salaries as input and store 
# them in a dictionary

num = int(input('Enter number of employees whose data to be stored: '))

count = 1
employee = dict()
while count <= num:
    name = input('Enter the name of employee: ')
    salary = int(input('Enter the salary: '))
    employee[name] = salary
    count += 1

print('\n\nEmployee Name \t Salary')
for k,v in employee.items():
    print(k,'\t\t', v)
    