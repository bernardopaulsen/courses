"""
Bernardo Paulsen

Exercise from class 165 from section 11
from Learn Complete Python In Simple Way.
"""

vowels = ['a','e','i','o','u']

word = 'paralelepipedo'
result = []
for ch in word:
    if ch in vowels:
        if ch not in result:
            result.append(ch)
print(result)

result = []
for ch in vowels:
    if ch in word:
        result.append(ch)
print(result)

result = [ch for ch in vowels if ch in word]
print(result)