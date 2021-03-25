"""
Bernardo Paulsen

Exercise from class 225 from section 15
from Learn Complete Python In Simple Way.
"""

# Anonymus fucntions
# - nameless function
# - instant use (one time usage)


# normal function
def square(x):
    return x*x

# anonymus function
sq = lambda x: x*x

print(sq(2))