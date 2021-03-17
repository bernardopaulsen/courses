"""
Bernardo Paulsen

Exercise from class 220 from section 15
from Learn Complete Python In Simple Way.
"""

a = 10
def f1():
    a = 20
    print(a)
def f2():
    print(a)
f1()
f2()

a = 10
def f3():
    global a
    a = 20
    print(a)
def f4():
    print(a)
f3()
f4()

def f5():
    global b
    b = 10
    print(b)
def f6():
    print(b)

f5()
f6()