"""
Bernardo Paulsen

Exercise from class 299 from section 18
from Learn Complete Python In Simple Way.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    def eat(self):
        print(f'{self.name}, age {self.age}, is eating.')

class Employee(Person):
    def __init__(self, name, age, eno):
        super().__init__(name, age)
        self.eno  = eno
    def work(self):
        print(f'Employee {self.name}, age {self.age}, No {self.eno}, is eating.')

a = Employee('Ber',24,1)
a.eat()
a.work()