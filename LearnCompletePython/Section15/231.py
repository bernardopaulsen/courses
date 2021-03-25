"""
Bernardo Paulsen

Exercise from class 229 from section 15
from Learn Complete Python In Simple Way.
"""
from functools import reduce

l = list(range(1,101))

print(reduce(lambda x,y: x+y,l))