"""
Bernardo Paulsen

Exercise from class 119 from section 9
from Learn Complete Python In Simple Way.
"""


s = 'Bernardo Paulsen'

print(s, id(s))

l1 = s.split()

l2 = s.split('r')

print('  '.join(l1))
print('  '.join(l2))