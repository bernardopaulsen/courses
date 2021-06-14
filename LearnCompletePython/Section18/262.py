"""
Bernardo Paulsen

Exercise from class 262 from section 18
from Learn Complete Python In Simple Way.
"""

class Test:
    def m(self):
        print('m')

a = Test()
a.m()

class Test2:
    def __init__(self):
        print('consctructor')

a = Test2()
a.__init__()