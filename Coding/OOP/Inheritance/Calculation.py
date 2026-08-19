class Calculation1:
    def sum(self, a, b):
        return a + b
    

class Calculation2:
    def multiplication(self, a, b):
        return a * b
    

class DerivedCalculation(Calculation1, Calculation2):
    def divide(self, a, b):
        return a / b
    
    
d = DerivedCalculation()

print(d.sum(8, 10))
print(d.multiplication(8, 10))
print(d.divide(8, 10))

print(issubclass(DerivedCalculation, Calculation2))#true
print(issubclass(Calculation1, Calculation2)) #false

print(isinstance(d, DerivedCalculation)) #True
print(isinstance(d, Calculation2)) #True
print(isinstance(d, Calculation1)) #True

