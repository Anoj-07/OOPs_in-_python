# Demonstrate polymorphism by defining a method fuel_type in both car and 
#electric Car but with different behaviours

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fuel_type(self):
        return "Petrol or Diesel"
    

class ElecticCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def fuel_type(self):
        return "Electic charge"
    

fuel = Car("BMW", "M3")
print(fuel.fuel_type())

electic = ElecticCar("Tesla", "S3", "200KWh")
print(electic.fuel_type())