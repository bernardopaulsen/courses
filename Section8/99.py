"""
Bernardo Paulsen

Exercise from class 99 from section 8
from Learn Complete Python In Simple Way.
"""

for i in range(3):
    for j in range(3):
        if i != j:
            print(i,j)
        else:
            break

print()

for i in range(3):
    for j in range(3):
        if i != j:
            print(i,j)
        else:
            continue