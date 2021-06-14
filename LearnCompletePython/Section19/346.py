"""
Bernardo Paulsen

Exercise from class 346 from section 19
from Learn Complete Python In Simple Way.
"""

try:
    a = int(input('Enter a integer:'))
    b = int(input('Enter a integer:'))
    print('Result', a/b)
except (ZeroDivisionError, ValueError) as msg:
    print(msg)
    print(msg.__class__)
    print(msg.__class__.__name__)