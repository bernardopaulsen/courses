"""
125: Reverse content of given string
"""
def reverse(string: str) -> str:
    return string[::-1]
"""
126: Reverse content of given string using reversed function
"""
def reverse_d(string: str) -> str:
    return ''.join(reversed(string))
"""
127: Reverse content of given string using while loop
"""
def reverse_loop(string: str) -> str:
    output = ''
    i      = len(string) - 1
    while i >= 0:
        output += string[i]
        i      -= 1
    return output
"""
128: Reverse order of words
"""
def reverse_words(string: str) -> str:
    return ' '.join(string.split()[::-1])
"""
129: Reverse each word in string
"""
def reverse_each(string: str) -> str:
    return ' '.join([s[::-1] for s in string.split()])
"""
130: Reverse content of every second word in string
"""
def reverse_second(string: str) -> str:
    l = []
    i = 0
    for s in string.split():
        i += 1
        if i%2:
            l.append(s)
        else:
            l.append(s[::-1])
    return ' '.join(l)
"""
131: Print odd and even characters separetely
"""
def even_odd(string: str) -> (str, str):
    return string[::2], string[1::2]
"""
132: Merge string taking characters alternatively
"""
def merge_alt(string1: str, string2: str):
    output = ''
    i      = 0
    while i < len(string1) or i < len(string2):
        if i < len(string1):
            output += string1[i]
        if i < len(string2):
            output += string2[i]
        i += 1
    return output
"""
133: First alphabet then numbers
"""
def separate(string):
    alphabets = []
    numbers   = []
    for character in string:
        if character.isalpha():
            alphabets.append(character)
        else:
            numbers.append(character)
    return ''.join(sorted(alphabets) + sorted(numbers))
"""
134: Count each character
"""
def count_order(string):
    chars = []
    nums  = []
    for character in string:
        if chars:
            if character != chars[-1]:
                chars.append(character)
                nums.append(1)
            else:
                nums[-1] += 1
        else:
            chars.append(character)
            nums.append(1)
    return chars,nums
"""
138: Remove duplicate characters
"""
def duplicate(string):
    output = ''
    for ch in string:
        if ch not in output:
            output += ch
    return output
"""
139: Count each character (ops, é o 141)
"""
def count(string):
    d = {}
    for ch in string:
        if ch in d.keys():
            d[ch] += 1
        else:
            d[ch] = 1
    return d
"""
144: Count vowels
"""
def count_vowels(string):
    vowels = ['a','e','i','o','u']
    d = {}
    for ch in string:
        low = ch.lower()
        if low in vowels:
            if low in d.keys():
                d[low] += 1
            else:
                d[low] = 1
    return d
"""
145: Anagrams
"""
def anagram(string1, string2):
    if sorted(string1) == sorted(string2):
        return True
    else:
        return False
"""
146: Palindrome
"""
def palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


"""
Assertion tests
"""

assert 'oi'                     == reverse('io')
assert 'oi'                     == reverse_d('io')
assert 'oi'                     == reverse_loop('io')
assert 'a e i o u'              == reverse_words('u o i e a')
assert 'ai ie ii io ui'         == reverse_second('ai ei ii oi ui')
assert ('brad', 'enro')         == even_odd('bernardo')
assert 'bernardo'               == merge_alt('brad', 'enro')
assert (['a', 'b'], [3, 2])     == count_order('aaabb')
assert 'bernado'                == duplicate('bernardo')
assert {'a': 6, 'b': 4}         == count('aaabbaaabb')
assert {'e': 1, 'a': 1, 'o': 1} == count_vowels('bernardo')
assert True                     == anagram('ab','ba')
assert True                     == palindrome('arara')


