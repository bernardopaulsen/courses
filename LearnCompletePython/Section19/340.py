"""
Bernardo Paulsen

Exercise from class 340 from section 19
from Learn Complete Python In Simple Way.
"""

try:
    print(10/0)
except ZeroDivisionError as msg:
    print(msg)
    print(msg.__class__)
    print(msg.__class__.__name__)
