"""
Title      : bermath
Description: Simple math functions.
Author     : Bernardo Paulsen
Version    : 1.0.0
"""

x = 888
y = 999

def add(a,b):
    """Adds two numbers"""
    return a+b

def product(a,b):
    """Returns prodcut of two numbers"""
    return a*b

if __name__ == "__main__":
    assert add(1,2)     == 3
    assert product(1,2) == 2
