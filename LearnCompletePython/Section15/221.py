"""
Bernardo Paulsen

Exercise from class 221 from section 15
from Learn Complete Python In Simple Way.
"""
def f1():
    global a
    print(a)
    a = 20
    print(a)
a = 10
f1()

def f2():
    a = 10
    print(a)
    print(globals().get('a'))

f2()