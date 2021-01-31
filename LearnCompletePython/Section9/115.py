"""
Bernardo Paulsen

Exercise from class 115 from section 9
from Learn Complete Python In Simple Way.
"""

s = ' Bernardo Paulsen '

print(s)
print(s.find('r'))
print(s.rfind('r'))
print(s.index('r'))
print(s.rindex('r'))

try:
    s.index('z')
except ValueError:
    print('opa')
try:
    s.index('B',4,1000)
except ValueError:
    print('eita')