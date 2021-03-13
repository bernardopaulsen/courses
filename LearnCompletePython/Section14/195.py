"""
Bernardo Paulsen

Exercise from class 195 from section 14
from Learn Complete Python In Simple Way.
"""

d = {0: 'a', 1: 'b'}

print(d.pop(0))
print(d)

d = {0: 'a', 1: 'b'}

print(d.pop(2,'ops'))

print(d.popitem())
print(d)
print(d.popitem())
print(d)
print(d.popitem())