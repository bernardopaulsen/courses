"""
Bernardo Paulsen

Exercise from class 105 from section 8
from Learn Complete Python In Simple Way.
"""

def is_prime(number):
    for i in range(2,number//2+1):
        if number%i == 0:
            return False
    return True

def get_primes(n):
    primes = 0
    number = 0
    while primes < n:
        number += 1
        if is_prime(number):
            print(number)
            primes += 1


a = int(input('How many prime numbers? '))
get_primes(a)