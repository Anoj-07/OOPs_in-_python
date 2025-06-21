from abc import ABC, abstractmethod

#abstact class
class Animal(ABC):
    #abstract method
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Using the abstract class
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.sound())


#Abstraction in Python is a concept in object-oriented programming that focuses on hiding the implementation details of a class or method while exposing only the essential features.
# In Python, we can achieve abstraction using abstract classes and methods.