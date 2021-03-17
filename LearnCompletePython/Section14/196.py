"""
Bernardo Paulsen

Exercise from class 195 from section 14
from Learn Complete Python In Simple Way.
"""

d = {0: 'a'}

print(d)

d[0] = 'b'

print(d)

print(d.setdefault(0,'c'))

print(d)

print(d.setdefault(1,'c'))

d1 = {0:1}
d2 = d1
d3 = d2.copy()

d2[0] = 2

print(d1)
print(d2)
print(d3)