"""
Bernardo Paulsen

Exercise from class 151 from section 11
from Learn Complete Python In Simple Way.
"""

l = [0,1,2,3,4,5,6,7,8,9,10]

# ACCESS ELEMENTS WITH WHILE LOOP
i = 0
while i < len(l):
    print(l[i])
    i += 1

# ACCESS ELEMENTS WITH FOR LOOP
for x in l:
    print(x)

# PRINT ONLY EVEN NUMBERS
for x in l:
    if not x % 2:
        print(x)

# PRINT ONLY ODD NUMBERS
for x in l:
    if x % 2:
        print(x)

l = [10,10,30,40,50,60]

# PRINT IN REVERSE ORDER
length = len(l)
for i in range(length):
    print(f'The element at index {i} and -ve index {i-length} is {l[i]}.')