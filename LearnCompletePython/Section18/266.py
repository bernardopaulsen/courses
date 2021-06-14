"""
Bernardo Paulsen

Exercise from class 266 from section 18
from Learn Complete Python In Simple Way.
"""

def Student():
    SCHOOL = 'farroupilha'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def student_info(self):
        print(self.name, self.age)
    @classmethod
    def school_info(cls):
        print(self.SCHOOL)
    @staticmethod
    def info():
        print('static method')