"""
Bernardo Paulsen

Exercise from class 287 from section 18
from Learn Complete Python In Simple Way.
"""

class Human:
    def __init__(self,name):
        self.name = name
        self.head = self.Head()
    def info(self):
        print(f'Name: {self.name}')
        self.head.talk()
        self.head.brain.think()
    class Head:
        def __init__(self):
            self.brain = self.Brain()
        def talk(self):
            print('Talking...')
        class Brain:
            def think(self):
                print('Thinking...')

a = Human('ber')
a.info()