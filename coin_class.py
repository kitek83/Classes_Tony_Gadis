import random
class Coin:
    def __init__(self):
        self.coin = 'orzel'
    def toss(self):
        if random.randint(0,1) == 0:
            self.coin = 'orzel'
        else:
            self.coin = 'reszka'
    def result(self):
        return self.coin