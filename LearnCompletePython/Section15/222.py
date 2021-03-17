"""
Bernardo Paulsen

Exercise from class 222 from section 15
from Learn Complete Python In Simple Way.
"""

# Recursive functions

# Example: factorial
def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n-1)
    return result

print(factorial(3))