"""
Bernardo Paulsen

Exercise from class 218 from section 15
from Learn Complete Python In Simple Way.
"""

def f1(*y, x=10):
    print(y)
    print(x)

f1(10,20,30,x=40)

def f2(arg1, arg2, arg3=30, arg4=40):
    print(arg1,arg2,arg3,arg4)

f2(10,20)

f2(10,20,10,20)

f2(arg4=2,arg1=3,arg2=4)