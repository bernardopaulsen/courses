"""
Bernardo Paulsen

Exercise from class 176 from section 12
from Learn Complete Python In Simple Way.
"""

s = {10,20,30,40}
print(type(s))

l = [10,20,30]
t = (10,20,30)

s.add(t)
print(s)
#s.add(l)

d = {}
t = (10,20,30)
l = [10,20,30]
d[t] = 'A'
print(d)
#d[l] = 'B'