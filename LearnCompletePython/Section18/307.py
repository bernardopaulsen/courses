"""
Bernardo Paulsen

Exercise from class 307 from section 18
from Learn Complete Python In Simple Way.
"""

class A: pass
class B: pass
class C: pass
class D(A,B): pass
class E(B,C): pass
class F(D,E,C): pass

print(A.mro())
print(D.mro())
print(F.mro())