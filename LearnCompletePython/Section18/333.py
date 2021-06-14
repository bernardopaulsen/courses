"""
Bernardo Paulsen

Exercise from class 333 from section 18
from Learn Complete Python In Simple Way.
"""

class Test:
    def __init__(self):
        self.__a = 1
    def __m1(self):
        print("private method")
    def m2(self):
        self.__m1()
        print(self.__a)

a = Test()
a.m2()

a._Test__m1()
print(a._Test__a)