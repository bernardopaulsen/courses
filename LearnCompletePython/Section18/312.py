"""
Bernardo Paulsen

Exercise from class 312 from section 18
from Learn Complete Python In Simple Way.
"""
class A:
    def m1(self):
        print('A')
class B(A):
    def m1(self):
        print('B')
class C(B):
    def m1(self):
        print('C')
class D(C):
    def m1(self):
        print('D')
class E(D):
    def m1(self):
        A.m1(self)
        super(C,self).m1()
        C.m1(self)
        super().m1()

a = E()
a.m1()