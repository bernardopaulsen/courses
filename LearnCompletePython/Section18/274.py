"""
Bernardo Paulsen

Exercise from class 274 from section 18
from Learn Complete Python In Simple Way.
"""

class Test:
    a = 10
    b = 20
    @classmethod
    def m1(cls):
        del cls.a
        del Test.b

a = Test
a.m1()
print(Test.__dict__)