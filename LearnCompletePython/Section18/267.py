"""
Bernardo Paulsen

Exercise from class 267 from section 18
from Learn Complete Python In Simple Way.
"""

class Test():
    def __init__(self):
        self.n = 1
    def upper(self):
        self.x  = 10

a = Test()

a.upper()

a.y = 100

print(a.__dict__)