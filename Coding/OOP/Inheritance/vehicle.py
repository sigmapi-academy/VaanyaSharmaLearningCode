class Vehicle:
    def start(self):
        print("vehicle started")
        
    def stop(self):
        print("vehicle stopped")
        

class Car(Vehicle):
    def drive(self):
        print("Car is driving")
        
        
# main code

toyotacar = Car()
toyotacar.start()
toyotacar.drive()
toyotacar.stop()