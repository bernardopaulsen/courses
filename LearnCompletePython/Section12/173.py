"""
Bernardo Paulsen

Exercise from class 173 from section 12
from Learn Complete Python In Simple Way.
"""

t = (10,20,30)

r = reversed(t)
t1 = tuple(r)
print(t1)

l = sorted(t)
t2 = tuple(l)
print(t2)

print(max(t))
print(min(t))