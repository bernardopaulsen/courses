"""
Bernardo Paulsen

Exercise from class 269 from section 18
from Learn Complete Python In Simple Way.
"""

class Test:
    a = 10
    def __init__(self):
        Test.b = 20
    def f(self):
        Test.c = 30
    @classmethod
    def g(cls):
        cls.d = 40
        Test.e = 50

print(Test.__dict__)
t = Test()
print(t.__dict__)
t.f()
t.g()
print(t.__dict__)
Test.b = 20
print(Test.__dict__)