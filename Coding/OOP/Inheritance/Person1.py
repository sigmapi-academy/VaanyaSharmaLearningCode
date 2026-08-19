class Person:
# A constructor is a special method that is automatically 
# called when an object of a class is created. 
# It is mainly used to initialize the attributes of the object. 

# The constructor is defined using the __init __() method. It takes 
# self as a first parameter and can expect additional arguments 
# to set values.
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Student(Person):
    def __init__(self, name, age, roll_no, course):
        # super() is used to access members of the parent class.
        super().__init__(name, age)
        # self.name = name
        # self.age = age
        self.roll_no = roll_no
        self.course = course
        
        
s = Student("Rahul", 21, 101, "C++")
print(s.name) # paraent class instance variable
print(s.course) # child class instance variable
        