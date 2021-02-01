"""
Bernardo Paulsen

Exercise from class 157 from section 11
from Learn Complete Python In Simple Way.
"""

# REMOVE method
l  = [10,20,30]
print(l)
l.remove(10)
print(l)

l = [10,20,10]
print(l)
l.remove(10)
print(l)

# remove all occurrences
l = [2,2,3,3,3,4,4,4,4]
print(l)
x = 3
while True:
    if 3 in l:
        l.remove(x)
    else:
        break
print(l)

def remove_all(lis_t: list, x):
    while True:
        if x in lis_t:
            lis_t.remove(x)
        else:
        break