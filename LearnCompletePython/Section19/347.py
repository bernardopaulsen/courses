"""
Bernardo Paulsen

Exercise from class 347 from section 19
from Learn Complete Python In Simple Way.
"""

try:
    a = int(input('Enter a integer:'))
    b = int(input('Enter a integer:'))
    print('Result', a/b)
except ZeroDivisionError as msg:
    print(msg)
    print(msg.__class__)
    print(msg.__class__.__name__)
except:
    print('Other error')