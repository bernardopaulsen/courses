"""
Bernardo Paulsen

Exercise from class 219 from section 15
from Learn Complete Python In Simple Way.
"""

# Global variables
# variable declared outside function
def f1():
    print(a)
a = 1
f1()
a = 2
f1()

# Local variables
def f2():
    a = 2
    print(a)
a = 1
f2()