"""
Bernardo Paulsen

Exercise from class 185 from section 13
from Learn Complete Python In Simple Way.
"""

# cloning

s1 = {10,20,30}

s2 = s1
print(id(s1))
print(id(s2))
s2.add(40)
print(s1)

s3 = s1.copy()
print(id(s3))
s3.add(50)
print(s1)

#comprehension

s = {x*x for x in range(1,6)}
print(s)