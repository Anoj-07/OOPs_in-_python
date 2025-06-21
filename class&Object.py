# Create a car class attributes like brand and model. 
# Then create an instance of this class

class Car: # class
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Class Method and self
    def car_type(self):
        return f"{self.brand} {self.model}"


cars = Car("Audi", "R8") # new object
print(cars.car_type()) 
print(cars.model)

cars1 = Car("Roll Royas", "Phentom")
print(cars1.car_type()) # for whole data
print(cars1.model) # for accesing single data