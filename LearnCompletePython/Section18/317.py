"""
Bernardo Paulsen

Exercise from class 317 from section 18
from Learn Complete Python In Simple Way.
"""

# + -> __add__
# - -> __sub__
# * -> __mul__
# / -> __div__
# // -> __floordiv__
# % -> __mod__
# ** -> __power__
# += -> __iadd__
# -= -> __isub__
# < -> __lt__
# <= -> __le__
# == -> __eq__
# != -> __ne__

class Book:
    def __init__(self, pages):
        self.pages = pages
    def __gt__(self,other):
        return self.pages > other.pages

b1 = Book(100)
b2 = Book(200)

print(b1 > b2)
