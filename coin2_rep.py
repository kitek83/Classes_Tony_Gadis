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
def main():
    my_coin = Coin()
    print('The result of coin toss is:', my_coin.result())
    print('Simulating next toss:')
    my_coin.toss()
    #my_coin.coin = 'orzel'
    print('The result of coin toss is:', my_coin.result())

main()