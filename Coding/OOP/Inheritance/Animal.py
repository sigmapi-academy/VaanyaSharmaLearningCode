class Animal:
    
    def eat(self):
        print("Animal is eating")
        
        
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
        
class Cat(Animal):
    def meao(self):
        print("Cat is saying meao...meao")
        
class Puppy(Dog):
    def cryForMilk(self):
        print("Puppy crying for milk...")
                    
happy = Dog()
happy.eat()
happy.bark()

poppins = Cat()
poppins.eat()
poppins.meao()

troy = Puppy()
troy.cryForMilk()
troy.bark()
troy.eat()