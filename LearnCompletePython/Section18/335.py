"""
Bernardo Paulsen

Exercise from class 335 from section 18
from Learn Complete Python In Simple Way.
"""

class Account:
    def __init__(self, initial_balance):
        self.__balance = initial_balance
    def get_balance(self):
        if input("Type the password:") == "1234":
            print(f"The balance is: {self.__balance}")

a = Account(1000)
a.get_balance()