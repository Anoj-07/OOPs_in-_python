class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    @staticmethod  #static method # decorator
    def general_description():
        return "This is a car "


my_car = Car("tata", "safari")
my_car1 = Car("BMW", "M3")

my_car3 = Car.general_description()
print(my_car3)  #output: This is a car

