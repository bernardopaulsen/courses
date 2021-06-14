"""
Bernardo Paulsen

Exercise from class 305 from section 18
from Learn Complete Python In Simple Way.
"""

# HYBRID AND CYCLIC INHERITANCE

# HYBRID
class A1: pass
class A2: pass
class B(A1,A2): pass
class C(B): pass
class D1(C): pass
class D2(C): pass
class D3: pass
class E(D1,D2,D3): pass

# CYCLIC - not supported

print(E.mro())