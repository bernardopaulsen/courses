"""
Bernardo Paulsen

Exercise from class 285 from section 18
from Learn Complete Python In Simple Way.
"""

class University: # outer class
    class Department: # inner class
        pass

class Car: # outer class
    class Engine: # inner class
        pass

class Outer:
    def __init__(self):
        print('Outer class object creation')
    class Inner:
        def __init__(self):
            print('Inner class object creation')
        def m1(self):
            print('Inner class method')

o = Outer()
i = o.Inner()
i.m1()