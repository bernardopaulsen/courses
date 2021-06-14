"""
Bernardo Paulsen

Exercise from class 316 from section 18
from Learn Complete Python In Simple Way.
"""
# +
print(10 + 20)
print('a' + 'b')
# *
print(10 * 2)
print('a' * 2)

class Book:
    def __init__(self, pages):
        self.pages = pages
    def __add__(self,other):
        total = self.pages + other.pages
        return Book(total)

b1 = Book(100)
b2 = Book(200)
b3 = b1 + b2
print(b3.pages)