"""
Bernardo Paulsen

Exercise from class 320 from section 18
from Learn Complete Python In Simple Way.
"""

class Book:
    def __init__(self, pages):
        self.pages = pages
    def __add__(self, other):
        return Book(self.pages + other.pages)
    def __str__(self):
        return str(self.pages)
    def __mul__(self, other):
        return Book(self.pages * other.pages)

a = Book(100)
b = Book(200)
c = Book(300)
print(a+b*c)