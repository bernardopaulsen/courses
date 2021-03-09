"""
Bernardo Paulsen

Exercise from class 164 from section 11
from Learn Complete Python In Simple Way.
"""

l1 = [10,20,30,40]
l2 = [30,40,50,60]
l = [x for x in l1 if x not in l2]
print(l)
l = [x for x in l1 if x in l2]
print(l)

s = 'the quick brown fox jumps over the lazy dog'
words = s.split()
print(words)

l = [[x.upper(), len(x)] for x in words]
print(l)