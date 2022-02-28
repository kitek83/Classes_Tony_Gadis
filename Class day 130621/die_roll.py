from random import randint
class Die:
    def __init__(self,sides):
        self.sides = sides

    def random_num(self):
        for x in range(6):
            print((randint(1,6))
choice = Die('')
choice.random_num()
