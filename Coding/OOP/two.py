class Dog:
    species = "Canine" # Class attribute (shared by all dogs)
    
    def __init__(self, name, age):
        self.name = name # Instance attribute 
        self.age = age   # Instance attribute 
        
    def barks(self):
        print(f"{self.name} says Woof!")
        
        
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

print(f"Name: {dog1.name} and Age: {dog1.age}")
print(f"Name: {dog2.name} and Age: {dog2.age}")

dog1.barks() # Buddy says woof!
dog2.barks() # Lucy says woof!
