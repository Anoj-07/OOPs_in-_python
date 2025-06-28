# Hiding the internal data of a class and only allowing access through methods.
# why it : 1. to protect data  2. contorl acess 3. hide complexity

# -------------------------Access modifiers-------------------------------:
# Modifier	=>  Syntax => 	Meaning
# Public =>	name =>	Anyone can access
# Protected	=> _name =>	Intended to be used inside class & child class
# Private => __name	=> Should not be accessed from outside

# Bank Account Example:

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # Private Variable ( __name is used to indicate private)
        # We can only access Private Variable through get_balance(), deposit(), and withdraw().(functions)

    def deposite(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
    
    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)

print("Your total balance is(Before): ", acc.get_balance())

acc.deposite(1200)

print("Your total balance is(after): ", acc.get_balance())

# print(acc.__balance) => you cannot access private variable and use function to acess them like above


# ----------------------Getter and setter-----------------------------------
# They are speial methods to get or update private varibales.

class Student:
    def __init__(self, name):
        self.__name = name
    
    def get_name(self): # Getter (get_Anyname)
        return self.__name
    
    def set_name(self, new_name): # setter (set_Anyname)
        self.__name = new_name

s = Student("Anoj")
print(s.get_name())

s.set_name('Paran')

# Task:
# Create a class PasswordManager
# Make __password a private variable.

# Add:
# set_password(new_pass) to update password
# get_password() to get current password
# Do not allow empty passwords

class PasswordManger:
    def __init__(self, password):
        self.__password = password
    
    def set_password(self, new_pass):
        if new_pass:
            self.__password = new_pass
        else:
            print("Password cannot be empty.")
    
    def get_password(self):
        return self.__password
        # return '*' * len(self.__password)

pass_word = PasswordManger("Anoj@12345")
pass_word.set_password("Paran@11235")

print("Current Password: ", pass_word.get_password())