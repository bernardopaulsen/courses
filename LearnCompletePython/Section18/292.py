"""
Bernardo Paulsen

Exercise from class 292 from section 18
from Learn Complete Python In Simple Way.
"""
import time

class Test:
    def __init__(self):
        print('Object initiation')
    def __del__(self):
        print('Object deletion')

a = Test()
a = 1

a = Test()