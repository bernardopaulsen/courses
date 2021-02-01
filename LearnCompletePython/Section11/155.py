"""
Bernardo Paulsen

Exercise from class 155 from section 11
from Learn Complete Python In Simple Way.
"""

# APPEND function
l = []
for i in range(10):
    l.append(i)
print(l)

# INSERT function
for i in range(10):
    l.insert(i*2,i)
print(l)

l = []
for i in range(10):
    l.insert(0,i)
print(l)