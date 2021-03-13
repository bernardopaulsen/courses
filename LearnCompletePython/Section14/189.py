"""
Bernardo Paulsen

Exercise from class 189 from section 14
from Learn Complete Python In Simple Way.
"""

# how to access data from a dictionary

d = {0: 'ber', 1: 'ayn'}

print(d[0])

d[0] = 'leo'
d[3] = 'fred'

print(d)

del d[3]

print(d)

del d[0], d[1]

print(d)

