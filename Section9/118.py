"""
Bernardo Paulsen

Exercise from class 118 from section 9
from Learn Complete Python In Simple Way.
"""

def remove_spaces(string):
    return string.replace(' ','')

s = 'Bernardo Paulsen'
print(id(s))
s = s.replace('r','R')
print(id(s))
s = s.replace('l','L')
print(id(s))
s = remove_spaces(s)
print(id(s))

print(s)