"""
Bernardo Paulsen

Exercise from class 161 from section 11
from Learn Complete Python In Simple Way.
"""

l1 = [10,20,30,40]
l2 = l1
l2[0] = 77

print(l1)
print(l2)
print(l1 is l2)

l1 = [10,20,30,40]
l2 = l1[:]
l3 = l1.copy()
l2[0] = 77
print(l1)
print(l2)
print(l3)
print(l1 is l2)
print(l1 is l3)