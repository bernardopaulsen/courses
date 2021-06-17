"""
Bernardo Paulsen

Exercise from class 369 from section 20
from Learn Complete Python In Simple Way.
"""
import inspect

def getInfo():
    print(inspect.stack())

def f1():
    getInfo()

f1()