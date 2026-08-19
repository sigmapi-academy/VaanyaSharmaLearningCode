class Employee:
    
    def display(self):
        print("I am an employee")
        
    def work(self):
        print("Employee is working")
        
        
class Manager(Employee):
    pass
        
        
class Developer(Employee):
    pass
    

#main code

anil = Manager()

anil.display()
anil.work()

Trisha = Developer()
Trisha.display()
Trisha.work()