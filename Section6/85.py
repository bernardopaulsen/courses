"""
Bernardo Paulsen

Exercise from class 85 from section 6
from Learn Complete Python In Simple Way.
"""

for x in range(10):
    print('Hello, welcome to my loop')

for x in range(1,11):
    print(f'Hello, welcome to my loop. This is loop {x}')

for x in range(20):
    if x%2 != 0:
        print(x)

for x in range(1,21,2):
    print(x)

for x in range(10,0,-1):
    print(x)

lst = eval(input('Enter list of numbers '))
s = 0
for x in lst:
    s += 1
print('Number of elements:', s)
print('Sum of elements   :',sum(lst))
