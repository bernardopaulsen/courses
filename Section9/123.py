"""
Bernardo Paulsen

Exercise from class 123 from section 9
from Learn Complete Python In Simple Way.
"""


s = 'BerNardo PauLsen'

print(s.isalnum())
print(s.islower())
print(s.isupper())
print(s.isdigit())
print(s.istitle())
print(s.isspace())

s = s.replace(' ','').lower()

print(s.isalnum())
print(s.islower())