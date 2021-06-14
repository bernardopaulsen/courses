"""
Bernardo Paulsen

Exercise from class 294 from section 18
from Learn Complete Python In Simple Way.
"""
import sys

class First:
    def __init__(self):
        print('First - initiated')
        self.second = self.Second()
    def __del__(self):
        print('First - deleted')
    class Second:
        def __init__(self):
            print('Second - initiated')
        def __del__(self):
            print('Second - deleted')

a = First()
del a

class Test:
    def __init__(self):
        print('Init')
    def __del__(self):
        print('Del')

t1 = Test()
t2 = t1
t3 = t2
t4 = t3

print(sys.getrefcount(t1))

del t3, t4

print(sys.getrefcount(t1))
