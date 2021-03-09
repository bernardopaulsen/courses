"""
Bernardo Paulsen

Exercise from class 168 from section 12
from Learn Complete Python In Simple Way.
"""

t = ()
print(type(t))

l = [10]
t = tuple(l)
print(type(t))

t = tuple(range(1,11))
print(t)
print(type(t))

t = tuple('ber')
print(t)
print(type(t))