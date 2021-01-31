"""
Bernardo Paulsen

Exercise from class 153 from section 11
from Learn Complete Python In Simple Way.
"""

# EQUALITY OPERATOR
l1 = ['Dog', 'Cat']
l2 = ['Dog', 'Cat']
l3 = ['DOG', 'Cat']
l4 = ['Cat', 'Dog']

print(l1==l2)
print(l1==l3)
print(l1==l4)

# RELATIONAL OPERATORS
l1 = [10,20,30]
l2 = [50,60]
print(l1<l2)
print(l1<=l2)
print(l1>l2)
print(l1>=l2)

# MEMBERSHIP OPERATORS
l = [10,20,30]
print(10 in l)
print(15 in l)