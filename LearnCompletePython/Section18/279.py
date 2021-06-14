"""
Bernardo Paulsen

Exercise from class 279 from section 18
from Learn Complete Python In Simple Way.
"""

class Test:
    def setA(self,a):
        self.A = a
    def getA(self):
        return self.A

a = Test()
a.setA(10)
print(a.getA())