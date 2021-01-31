"""
Bernardo Paulsen

Exercise from class 117 from section 9
from Learn Complete Python In Simple Way.
"""

s = 'Bernardo Paulsen'

def find_all(string,sub):
    indexes = []
    find    = string.find(sub)
    while find != -1:
        indexes.append(find)
        find = string.find(sub,find+1)    
    return indexes

ind = find_all(s,'z')
print(ind)