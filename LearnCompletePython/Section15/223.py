"""
Bernardo Paulsen

Exercise from class 223 from section 15
from Learn Complete Python In Simple Way.
"""


def factorial(n):
    print(f'Execution of factorial function for n = {n}')
    if n == 0:
        result = 1
    else:
        result = n * factorial(n-1)
    print(f'Returning result for factorial of n = {n} ({result})')
    return result

print(factorial(3))