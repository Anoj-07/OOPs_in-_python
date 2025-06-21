#Modify the car class to encapsulation the brand attribute
# making it private and provide a getter method for it.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand # private attribute
        self.model = model
    

    #@property # getter method
    def get_brand(self):
        return f"{self.__brand} {self.model}"
    
    #@get_brand.setter # setter method
    def set_brand(self, brand):
        self.__brand = brand
       

car = Car("Tesla", "S class")
print(car.get_brand())

car.model = "P" # change model 

car.set_brand = "BMW" # change brand through setter method
print(car.get_brand())