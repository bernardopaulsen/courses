"""
Bernardo Paulsen

Exercise from class 325 from section 18
from Learn Complete Python In Simple Way.
"""

class Parent1:
    def __init__(self, a):
        print('Parent 1 constructor')
        self.a = a

class Parent2:
    def __init__(self, b):
        print('Parent 2 constructor')
        self.b = b

class Child(Parent1,Parent2):
    def __init__(self, a, b):
        print('Child Constructor')
        Parent1.__init__(self, a)
        Parent2.__init__(self, b)

a = Child(1,2)
print(a.a)
print(a.b)