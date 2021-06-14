"""
Bernardo Paulsen

Exercise from class 313 from section 18
from Learn Complete Python In Simple Way.
"""

class P:
    a = 888
    def __init__(self):
        print('Parent constructor')
        self.b = 999

class C(P):
    def __init__(self):
        self.b = 20

    def m1(self):
        print(self.b)

a = C()
a.m1()