"""
Bernardo Paulsen

Exercise from class 224 from section 15
from Learn Complete Python In Simple Way.
"""

# Max recursion depth: 950

def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n-1)
    return result

print(factorial(997))
print(factorial(998)) # RecursionError

