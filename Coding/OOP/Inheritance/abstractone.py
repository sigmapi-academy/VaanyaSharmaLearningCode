from abc import ABC, abstractmethod

#abstract base class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
#child class
class Car(Vehicle):
    # Abstract methods are always implemented inside a child class.
    # This is called method overriding.
    def start(self):
        print("Car is starting with a key ignition.")
        
    def stop(self):
        print("Car is stopping using the brake")
        
my_car = Car()
my_car.start()
my_car.stop()

my_vehicle = Vehicle()
my_vehicle.start()
my_vehicle.stop()