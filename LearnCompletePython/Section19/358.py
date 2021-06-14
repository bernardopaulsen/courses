"""
Bernardo Paulsen

Exercise from class 358 from section 19
from Learn Complete Python In Simple Way.
"""

class TooMuchGinException(Exception):
    def __init__(self, msg):
        self.msg = msg

raise TooMuchGinException("You won't handle it well, man.")


