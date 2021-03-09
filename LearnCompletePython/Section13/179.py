"""
Bernardo Paulsen

Exercise from class 179 from section 13
from Learn Complete Python In Simple Way.
"""

# SET
# 1. duplicates are not allowed
# 2. order is not applicable
# 3. without indexing or slicing concepts
# 4. {1,2,3}
# 5. heterogeneous objects allowed
# 6. mutable
# 7. methods: union, intersection, difference

s = set()
print(s)
print(type(s))

s.add(0)
print(s)
print(type(s))

s.add('a')
print(s)

s.add(0)
print(s)
