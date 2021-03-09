"""
Bernardo Paulsen

Exercise from class 162 from section 11
from Learn Complete Python In Simple Way.
"""

l = [10,20,[30,40]]
print(l[0])
print(l[1])
print(l[2])
print(l[2][0])
print(l[2][1])


l = [[10,20,30],[40,50,60],[70,80,90]]
print(l)

for x in l:
    print(x)

for x in l:
    for y in x:
        print(y, end=' ')
    print()