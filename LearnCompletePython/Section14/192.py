"""
Bernardo Paulsen

Exercise from class 192 from section 14
from Learn Complete Python In Simple Way.
"""

d = {0: 'a', 1: 'b'}

print(len(d))

print(d.get(0))
print(d.get(2))

print(d.get(2,'opa'))

d1 = {2: 'c', 3: 'd'}

d.update(d1)

print(d)