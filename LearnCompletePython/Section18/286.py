"""
Bernardo Paulsen

Exercise from class 286 from section 18
from Learn Complete Python In Simple Way.
"""

class Outer:
    def __init__(self):
        print('Outer class object creation')
    class Inner:
        def __init__(self):
            print('Inner class object creation')
        class InnerInner:
            def __init__(self):
                print('InnerInner class object creation')
            @staticmethod
            def m1():
                print('InnerInner class method')

o  = Outer()
i  = o.Inner()
ii = i.InnerInner()
ii.m1()

print()

Outer().Inner().InnerInner().m1()

print()

Outer.Inner.InnerInner.m1()