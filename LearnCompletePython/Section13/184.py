"""
Bernardo Paulsen

Exercise from class 184 from section 13
from Learn Complete Python In Simple Way.
"""

s1 = {10,20,30}
s2 = {30,40,50}

s3 = s1.union(s2)
print(s3)

s4 = s1.intersection(s2)
print(s4)

s5 = s1.difference(s2)
print(s5)

s6 = s1 - s2
print(s6)

s7 = s1.symmetric_difference(s2)
print(s7)

s8 = s1^s2
print(s8)