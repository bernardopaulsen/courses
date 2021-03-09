"""
Bernardo Paulsen

Exercise from class 174 from section 12
from Learn Complete Python In Simple Way.
"""
a = 10
b = 20
c = 30
d = 40

t = a,b,c,d

a,b,c,d = t

print(a,b,c,d)

a, *b = t

print(a,b)