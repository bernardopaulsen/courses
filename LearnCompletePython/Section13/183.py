"""
Bernardo Paulsen

Exercise from class 183 from section 13
from Learn Complete Python In Simple Way.
"""

s = {10,20,30}
s.remove(10)
print(s)

s = {10,20,30}
s.discard(30)
print(s)
s.discard(50)
print(s)

s = {10,20,30}
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)

s = {10,20,30}
print(s)
s.clear()
print(s)