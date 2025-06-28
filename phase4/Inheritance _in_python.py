# Inheritance allows a class (child class) to acquire properties and methods of another class (parent class). It supports hierarchical classification and promotes code reuse.

# Types of Inheritance:
# Single Inheritance: A child class inherits from a single parent class.
# Multiple Inheritance: A child class inherits from more than one parent class.
# Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another class.
# Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
# Hybrid Inheritance: A combination of two or more types of inheritance.


# Type => 	Structure =>	Example
# Single Inheritance =>	 A → B	=>   Animal → Dog
# Multilevel Inheritance  =>	A → B → C    => Animal → Mammal → Human
# Multiple Inheritance =>  A + B → C   => 	Father + Mother → Child
# Hierarchical Inheritance =>	A → B, A → C    =>	Animal → Dog, Animal → Cat

# Basic Syntax:

# 1. Single Inheritance:
class Parent:
    def speak(self):
        print("I can speak !") # second this will be executed

class Child(Parent):  # Child class inherits from Parent class
    print("I am a child class !") # first this will be executed

print("\n==================")
c = Child()
c.speak()

# Example of Single Inheritance with __init__() method:
# Parent Class: Person
class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

# Child Class: Employee
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        super().__init__(name, idnumber)  # Calls Person's __init__()
        self.salary = salary
        self.post = post



# 2. Multilevel Inheritance:

# Animal => Mammal => Human

class Animal:   
    def breathe(self):
        print("Breathing...")
    
class Mammal(Animal):
    def walk(self):
        print("Walking...")

class Human(Mammal):
    def speak(self):
        print('self can speak !')

print("\n==================")
h = Human()

h.breathe()  # Inherited from Animal
h.walk()     # Inherited from Mammal
h.speak()   # Defined in Human


# 3. Multiple  Inheritance:

# Father, Mother => Child

class Father:
    def skills(self):
        print("I can cook and drive !")

class Mother:
    def cooking(self):
        print("I can sing and dance !")

class child(Father, Mother):
    def hobby(self):
        print("I love coding !")

print("\n==================")

c = child()
c.skills() # Will call the skills method from Father class


# => Method Overriding in Multiple Inheritance:
# A child class can change a method from the parent class.

class Animal:
    def sound(self):
        print("some sound")

class Dog(Animal):
    def sound(self): # overridden method
        print("Bark...")

print("\n==================")
d = Dog()
d.sound()  # This will call the overridden method in Dog class


# Super() Function :
# Calls the parent class method.

class Parent:
    def hello(self):
        print("Hello from parent ")

class child(Parent):
    def hello(self):
        super().hello()
        print('hello form child')

print('\n==================')
c = child()
c.hello() # This will call the hello method from Parent class and then from child class

# 4. Hierarchical Inheritance:
# Parent => Child1, Child2

class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def bark(self):
        print('barking...')

class Cat(Animal):
    def meow(self):
        print("Meowing...")

print("\n==================")
d = Dog()
c = Cat()

d.sound()  # Inherited from Animal
d.bark()   # Defined in Dog
c.sound()  # Inherited from Animal  
c.meow()   # Defined in Cat 


# Task :

class Vehicle:
    def start(self):
        print('Vehicle started')

class Car(Vehicle):
    def drive(self):
        print('Car is driving')
print("\n==================")
c = Car()
c.start()
c.drive()



# THIS IS OPTIONAL:

# ✅ 7. Use Type Hints
# Helps editors, tools, and future readers.

# def add(self, a: int, b: int) -> int:
#     return a + b


# 2. Add type hints for extra clarity (used by professionals):

# class Vehicle:
#     def start(self) -> None: # mention return type -> None or any data type
#         print("Vehicle started")

# class Car(Vehicle):
#     def drive(self) -> None:
#         print("Car is driving")