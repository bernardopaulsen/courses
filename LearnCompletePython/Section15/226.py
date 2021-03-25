"""
Bernardo Paulsen

Exercise from class 226 from section 15
from Learn Complete Python In Simple Way.
"""

s = lambda a,b: a + b
b = lambda a,b: a if a > b else b if b > a else None

print(s(1,2))
print(b(3,4))
print(b(3,3))