"""
Bernardo Paulsen

Exercise from class 113 from section 9
from Learn Complete Python In Simple Way.
"""

s = ' Bernardo Paulsen '

s *= 3

print(s)
print('Ber' in s)

s = s.lstrip()
s = s.rstrip()
s = s.strip()

print(s)