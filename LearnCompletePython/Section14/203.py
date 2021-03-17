"""
Bernardo Paulsen

Exercise from class 203 from section 14
from Learn Complete Python In Simple Way.
"""

# list merging
l1 = [10,20]
l2 = [30,40]
l3 = l1 + l2
l4 = [*l1, *l2]

# tuple merging
t1 = (10,20)
t2 = (30,40)
t3 = t1 + t2
t4 = (*t1, *t2)

# set merging
s1 = {10,20}
s2 = {30,40}
s3 = s1 + s2
s3 = {*s1, *s2}

# dict merging
d1 = {1:'a',2:'b'}
d2 = {3:'c',4:'d'}
d3 = {**d1,**d2}