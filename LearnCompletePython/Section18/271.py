"""
Bernardo Paulsen

Exercise from class 270 from section 18
from Learn Complete Python In Simple Way.
"""

class Test:
    a = 10
    def __init__(self):
        Test.a = 20
    def m1(self):
        Test.a = 30
    @classmethod
    def cm1(cls):
        cls.a = 40
    @staticmethod
    def sm1():
        Test.a = 50