#Add a class variable to car that keeps track of the number of cars created


class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        # self.total_car or, 
        Car.total_car += 1
    
Car("Audi", "R8")
Car("piggani" , "k8")
Car("Paran", "2")

print(Car.total_car)

