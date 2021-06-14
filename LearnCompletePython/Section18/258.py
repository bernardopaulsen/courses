"""
Bernardo Paulsen

Exercise from class 258 from section 18
from Learn Complete Python In Simple Way.
"""

class Student:
    """This class was developed by Ber"""
    def __init__(self, name, marks):
        self.name  = name
        self.marks = marks
    def talk(self):
        """Description of itself"""
        print(f"My name is {self.name}")
        print(f"My marks are {self.marks}")

#print(Student.__doc__)
#help(Student)

a = Student('a',1)
b = Student('b',2)

a.talk()
b.talk()

