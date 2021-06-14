"""
Bernardo Paulsen

Exercise from class 289 from section 18
from Learn Complete Python In Simple Way.
"""

class Test:
    def m1(self):
        def calc(a,b):
            print(f'Sum    : {a+b}')
            print(f'Product: {a*b}')
        calc(10,20)
        calc(100,200)

a = Test()
a.m1()