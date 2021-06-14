"""
Bernardo Paulsen

Exercise from class 293 from section 18
from Learn Complete Python In Simple Way.
"""
import time

class Test:
    def __init__(self):
        print('Init')
    def __del__(self):
        print('del')

a = Test()
b = a
c = b

del a
del b

print('Object not destroyed after deleting a & b')

l = [Test(), Test(), Test()]

l[0] = None

print('End of application.')