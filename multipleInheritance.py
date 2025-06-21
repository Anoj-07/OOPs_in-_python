class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Battery:
    def battery_info(self):
        return "This is a battery"


class Engine:
    def engine_info(self):
        return "This is an enginee"


#child class
class ElectricCar(Battery, Engine, Car):
    pass

my_car = ElectricCar("Tesla", "S3")

print(my_car.battery_info())
print(my_car.engine_info())