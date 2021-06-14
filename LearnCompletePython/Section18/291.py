"""
Bernardo Paulsen

Exercise from class 291 from section 18
from Learn Complete Python In Simple Way.
"""

import gc

print(gc.isenabled())

gc.disable()
print(gc.isenabled())

gc.enable()
print(gc.isenabled())