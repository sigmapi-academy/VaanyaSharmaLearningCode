class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display_person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        
class Student(Person):
    def __init__(self, roll_no, course, name, age):
        super().__init__(name, age)
        #additional code
        self.roll_no = roll_no
        self.course = course
        
    def display_student(self):
        print(f"Roll No. : {self.roll_no}")
        print(f"Course: {self.course}")
        
        
# main code
s = Student(101, 'Python','Vaanya', 12)

s.display_person()
s.display_student()