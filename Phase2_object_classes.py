# what is class?
# class is a blueprint for creating objects

class cake:
    def __init__(self, flavor):
        self.flavour = flavor

# what is object?
# object is an instance of a class
# An object is a real thing created from a class.

cake1 = cake('chocolate')
cake2 = cake('vanilla')
print(cake1.flavour)

# __int__() method is a constructor
# it is called when an object is created from a class
# __init__() is like building and decorating your toy right after buying it.
# self refers to this object.
# name is the value we pass in.


# ---------Adding methods to class------------
class cake:
    def __init__(self, flavour):
        self.flavour = flavour
    
    def describe(self):
        return f'This is a {self.flavour} cake.'


cake1 = cake('chocolate')
print(cake1.describe())

#--------------------class varibale vs instance(self) variable-------------------
class student:
    school = 'Nandeshwar High School'  # class variable

    def __init__(self, name):
        self.name = name

s1 = student('Anoj')

print(s1.school) # class variable accessed through instance
print(s1.name)  # class variable accessed through class

#---------------------Task 1 ----------------------------------------
# Create a class called 'Car' with the following attributes:    
#Add:
# brand and model as instance variables.
# A method called drive() that prints "The [brand] [model] is driving!".

class Car:
    def __init__(self, brand, model):
        self.brand= brand
        self.model = model

    def drive(self):
        return f"The {self.brand} {self.model} is driving!"
    

car_brand = Car('Tesla', ' Model S')
print(car_brand.drive())

