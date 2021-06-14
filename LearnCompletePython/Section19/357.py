"""
Bernardo Paulsen

Exercise from class 357 from section 19
from Learn Complete Python In Simple Way.
"""

def withdraw(amount, balance):
    if  amount > balance:
        raise InSufficientFundsException()
    else:
        pass