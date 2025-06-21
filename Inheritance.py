#Create an ElectricCar class that inherits from the car class
#and has an additional attribute

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Electic_car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model) #super() keyword is used to access attibutes and method of parent class
        self.battery = battery_size
    
    def full(self):
        return f"{self.brand} {self.model} {self.battery}"
    


cars = Electic_car("tesla", "S_class", "2000000kwh")
print(cars.full())

#isinstance() function
print(isinstance(cars, Car))
print(isinstance(cars, Electic_car))


#----------------------------------------------------------
# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def personName(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduate = year

#     def wlcome(self):
#         print(self.graduate)


# x= Student("Anoj", "Rawal", 2025)
# x.personName()
# x.wlcome()

