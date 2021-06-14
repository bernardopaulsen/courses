"""
Bernardo Paulsen

Exercise from class 328 from section 18
from Learn Complete Python In Simple Way.
"""
from abc import abstractmethod, ABC

class Test1:
    @abstractmethod
    def m1(self):
        pass

class Vehicle(ABC):
    @abstractmethod
    def m1(self):
        pass

class Car(Vehicle):
    def m1(self):
        return 4





a = Test1()
b = Car()