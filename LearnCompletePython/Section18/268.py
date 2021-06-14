"""
Bernardo Paulsen

Exercise from class 268 from section 18
from Learn Complete Python In Simple Way.
"""

class Test():
    def __init__(self):
        self.a = 10
        self.b = 20
    def f1(self):
        del self.b

a = Test()
print(a.__dict__)
del a.a
print(a.__dict__)
a.f1()
print(a.__dict__)