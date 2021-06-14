"""
Bernardo Paulsen

Exercise from class 310 from section 18
from Learn Complete Python In Simple Way.
"""

class P:
    def m1(self):
        print('Parent method.')

class C(P):
    def m1(self):
        super().m1()
        print('Child method.')

a = C()
a.m1()