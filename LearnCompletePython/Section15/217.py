"""
Bernardo Paulsen

Exercise from class 217 from section 15
from Learn Complete Python In Simple Way.
"""

# ARGS
# variable length arguments
# arguments become tuple
def f1(*args):
    print(args)
f1(10,20,30)

# KWARGS
# variable length key-word arguments
# arguments become dictionary
def f2(**kwargs):
    print(kwargs)
f2(a=10, b=20, c=30)

# BOTH
def f3(*args,**kwargs):
    print(args)
    print(kwargs)
f3(10,20,a=30,b=40)

