# 1. Data Structure: Use a dictionary students where each entry is 
# {student_id: (name, [score1, score2, score3, score4, score5])}

#  get_top_students(students, n): Return top n students by average

def addNewStudent(students:dict):
    sid = input("Enter student id: ")
    name = input("Enter name: ")
    score = eval(input("Enter marks of 5 subjects in list form: "))
    # adding new student in dictionary
    if sid in students:
        print('Duplicate sid')
        print()
    else: #create new element in the dictionary
        students[sid] =(name, score)
    
def get_top_students(students:dict, n:int): #Return top n students by average
    # traverse the student to calculate the average
    sid_avg=[]
    for k, v in students.items():
        sum = 0
        for score in v[1]:
            sum += score
        avg = sum / 5.0
        
        pos = 0
        for am in sid_avg:
            if am[1] < avg:
                break
            pos += 1
            
        sid_avg.insert(pos,(k,avg))
    
    top_n = dict()
    for id in sid_avg:
        if n > 0:
            top_n[id[0]] = students[id[0]]
            n -= 1
                    
    return top_n
    # print(sid_avg)
    
#main code
students = dict()
while True:
    print("Press 1 to store a new student: ")
    print("Press 2 to find n top average students" )
    print("Press 0 to exit")
    print("Enter your choice: ")
    ch = int(input())
    match ch:
        case 1:
            addNewStudent(students)
        case 2:
            top_n = get_top_students(students, 3)
            for k, v in top_n.items():
                print(k,v)
        case 0:
            print("Have a wonderful evening")
            quit() #to close the execution
