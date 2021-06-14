"""
Bernardo Paulsen

Exercise from class 334 from section 18
from Learn Complete Python In Simple Way.
"""

class Test:
    def __init__(self):
        self._a = 1
    def _m1(self):
        print("protected method")

class SubTest(Test):
    def m2(self):
        self._m1()
        print(self._a)

t = SubTest()
t.m2()

t._m1()
print(t._a)