"""
Bernardo Paulsen

Exercise from class 319 from section 18
from Learn Complete Python In Simple Way.
"""

class Student:
    def __init__(self, name, marks):
        self.name  = name
        self.marks = marks
    def __str__(self):
        return f"{self.name}: {self.marks}"

a = Student('Ber',.9)
print(a)