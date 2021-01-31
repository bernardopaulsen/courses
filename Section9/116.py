"""
Bernardo Paulsen

Exercise from class 116 from section 9
from Learn Complete Python In Simple Way.
"""

s = 'Bernardo Paulsen'

print(s.count('r',4,1000))
print(s.count('z'))

while True:
    email = input('Enter your gmail: ')
    if email.count('@gmail.com') == 1 and email.find('@') > 0:
        print('Thanks!')
        break
    else:
        print('Invalid.')