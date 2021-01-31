"""
Bernardo Paulsen

Exercise from class 108 from section 9
from Learn Complete Python In Simple Way.
"""

string = input('Enter word: ')
lenght = len(string)


i = 0
for s in string:
    print(f'The character at indexes {i} and {i-lenght} is {s}')
    i += 1