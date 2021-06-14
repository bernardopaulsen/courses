"""
Bernardo Paulsen

Exercise from class 314 from section 18
from Learn Complete Python In Simple Way.
"""

class P:
    def __init__(self):
        print('Parent constructor')
    def m1(self):
        print('Parent instance method')
    @classmethod
    def m2(cls):
        print('Parent class method')
    @staticmethod
    def m3():
        print('Parent static method')

class C(P):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
    def m1(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
    @classmethod
    def m2(cls):
        super(C,cls).__init__(cls)
        super(C,cls).m1(cls)
        super().m2()
        super().m3()
    @staticmethod
    def m3():
        #super().__init__()
        #super().m1()
        super(C,C).m2()
        super(C,C).m3()

a = C()
print()
a.m1()
print()
a.m2()
print()
a.m3()
