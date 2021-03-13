"""
Bernardo Paulsen

Exercise from class 193 from section 14
from Learn Complete Python In Simple Way.
"""

d = {0: 'a', 1: 'b'}

k = d.keys()
print(k)
for key in k:
    print(key)

v = d.values()
print(v)
for value in v:
    print(value)

i = d.items()
print(i)
for key, value in i:
    print(key, value)