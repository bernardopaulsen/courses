"""
Bernardo Paulsen

Exercise from class 163 from section 11
from Learn Complete Python In Simple Way.
"""

l = []
for i in range(1,11):
    l.append(i)
print(l)

l = [i for i in range(1,11)]
print(l)

l = [i*i for i in range(1,11)]
print(l)

l = [i*i for i in range(1,11) if not i%2]
print(l)
