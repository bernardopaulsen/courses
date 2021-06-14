"""
Bernardo Paulsen

Exercise from class 270 from section 18
from Learn Complete Python In Simple Way.
"""

class Test:
    a = 10
    def __init__(self):
        print(self.a)
        print(Test.a)
    def m1(self):
        print(self.a)
        print(Test.a)
    @classmethod
    def cm1(cls):
        print(cls.a)
        print(Test.a)
    @staticmethod
    def sm1():
        print(Test.a)

a = Test()
a.m1()
a.cm1()
a.sm1()