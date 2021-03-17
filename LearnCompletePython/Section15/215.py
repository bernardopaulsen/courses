"""
Bernardo Paulsen

Exercise from class 215 from section 15
from Learn Complete Python In Simple Way.
"""

def f1(*n):
    print(len(n))


f1(1)

f1(1,2,3,4)

def f2(x,*y):
    print(x)
    print(len(y))

f2(1,2)

f2(1,2,3,4,5)