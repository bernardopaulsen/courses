"""
Bernardo Paulsen

Exercise from class 256 from section 18
from Learn Complete Python In Simple Way.
"""

class Student:
    """This class was developed by Ber"""
    def __init__(self):
        self.name  = 'Ber'
        self.marks = 100
    def talk(self):
        """Description of itself"""
        print(f"My name is {self.name}")
        print(f"My marks are {self.marks}")

#print(Student.__doc__)
#help(Student)

b = Student()
print(b.name)
print(b.marks)
b.talk()

