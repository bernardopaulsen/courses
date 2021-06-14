"""
Bernardo Paulsen

Exercise from class 280 from section 18
from Learn Complete Python In Simple Way.
"""

class Test:
    count = 0
    def __init__(self):
        Test.count += 1
    @classmethod
    def getNumber(cls):
        print(cls.count)

a = Test()
b = Test()
Test.getNumber()