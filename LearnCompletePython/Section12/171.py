"""
Bernardo Paulsen

Exercise from class 171 from section 12
from Learn Complete Python In Simple Way.
"""

t1 = ('oi','tchau')
t2 = ('oi','tchau')
t3 = ('oi','TCHAU')

print(t1 == t2)
print(t1 == t3)

print(t1 is t2)

t1 = (10,20,30)
t2 = (11,20,30)

print(t1 < t2)

t1 = (10,20,30)
t2 = (10,10,70)

print(t1 > t2)

t = (10,20,30)

print(10 in t)
