"""
Bernardo Paulsen

Exercise from class 100 from section 8
from Learn Complete Python In Simple Way.
"""

items = [10,20,30,40,50,600,70]

for item in items:
    if item >= 500:
        print('Invalid')
        break
    print('Processing')
else:
    print('All values were valid')

for item in items:
    if item >= 500:
        print('Invalid')
        continue
    print('Processing')
else:
    print('All valid values processed')