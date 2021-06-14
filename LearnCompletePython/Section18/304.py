"""
Bernardo Paulsen

Exercise from class 304 from section 18
from Learn Complete Python In Simple Way.
"""

# MULTIPLE INHERITANCE

class P1:
    def m1(self):
        print('P1')
class P2:
    def m1(self):
        print('P2')
class C1(P1,P2):
    pass
class C2(P2,P1):
    pass

a = C1()
a.m1()
a = C2()
a.m1()