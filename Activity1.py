class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class Car(Vehicle):
    pass
Taxi=Car("Taxi Toyota", 180, 32)
print("Vehicle name:",Taxi.name, "Speed:",Taxi.max_speed,"Vehicle mileage:",Taxi.mileage)
