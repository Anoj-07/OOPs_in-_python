# "One name, many forms" — the same method or function can do different things depending on the object.
# 🔁 Imagine pressing the same button on a TV remote:
# On TV → changes channel
# On AC → changes temperature
# Same name, different behavior.

# ✅ Where Is Polymorphism Used?
# Same method name in different classes (sound(), draw(), etc.)
# Functions that work on multiple object types
# Operator overloading (+ works for numbers and strings)



# | Type                                  | Meaning                                | Python Supports? |
# | ------------------------------------- | -------------------------------------- | ---------------- |
# | **Compile-time** (Method overloading) | Same method name with different params | ❌ Not natively   |
# | **Run-time** (Method overriding)      | Child class changes parent method      | ✅ Yes            |
# | **Duck Typing**                       | If it behaves like a duck, it’s a duck | ✅ Yes            |

# 1. Mehtod overriding (Run time Polymorphism)
# Child class changes behavior of parent class method

class Animal:
    def sound(self):
        print("Some sound ")

class Dog(Animal):
    def sound(self):
        print("Bark !")

class Cat(Animal):
    def sound(self):
        print("Meow !")

a = Animal()
d = Dog()
c = Cat()

a.sound()  # Output: Some sound
d.sound()  # Output: Bark!
c.sound()  # Output: Meow !

# 2. Duck Typing (Dynamic Polymorphism)
# If it walks like a duck, quacks like a duck, it’s a duck 🦆

class Duck:
    def talk(self):
        print('Quack !')

class Human:
    def talk(self):
        print("Hello !")

def speak_anynone(entity):
    entity.talk()

speak_anynone(Duck())
speak_anynone(Human())  # Output: Hello !

# 🚀 We don’t care what type it is — we only care that it has talk() method.
