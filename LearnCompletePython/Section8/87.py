"""
Bernardo Paulsen

Exercise from class 86 from section 6
from Learn Complete Python In Simple Way.
"""

n = int(input('Enter number:'))
s = 0
i = 0
while i <= n:
    s += i
    i += 1
print('Sum:',s)

word = 'not yes'
while word != 'yes':
    word = input("Enter 'yes'")
print('Correct!')