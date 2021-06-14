"""
Bernardo Paulsen

Exercise from class 298 from section 18
from Learn Complete Python In Simple Way.
"""

class Parent:
    A = 1
    def __init__(self):
        print('parent init')
        self.b = 2
    def m1(self):
        print('parent method!')
    @classmethod
    def m3(cls):
        print('parent class method!')

class Child(Parent):
    pass

a = Child()
print(a.A)
print(a.b)
a.m1()
a.m3()