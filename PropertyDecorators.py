class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
    
    #To stop change od attribute value (property Decorator)

    def full(self):
        return f"{self.__brand} {self.__model}"
    

    @property #getter decorator
    def model(self):
        return self.__model
    
    def ser_mode(self, model):
        self.__model = model

# it is only readable and access through getter
my_car = Car("Porshe", "AP")
my_car.__model = "PA" # it will not chage 
print(my_car.model)