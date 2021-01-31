"""
Bernardo Paulsen

Exercise from class 102 from section 8
from Learn Complete Python In Simple Way.
"""

x = 10

print(x)

del x

a = 'hello'
b = a
c = b
print(id(a))
print(id(b))
print(id(c))

del a, b

print(c)

a = b = c = 'hello'

print(id(a))
print(id(b))
print(id(c))