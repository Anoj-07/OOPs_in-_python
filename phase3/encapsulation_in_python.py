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
