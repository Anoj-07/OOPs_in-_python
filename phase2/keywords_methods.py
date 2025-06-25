# __init__() method => The Constructor => it is like building and decorating your toy right after buying it.
# self keyword => Think of self as me inside the object.

class Dog:
    def __init__(self, name):
        self.name = name

# creating object
cat1 = Dog("Tommy")
print(cat1.name)