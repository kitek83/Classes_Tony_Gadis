import random
class Coin:
    def __init__(self):
        self.sideup = 'orzel'
    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = 'orzel'
        else:
            self.sideup = 'reszka'
    def get_sideup(self):
        return self.sideup
def main():
    my_coin = Coin()
    print('Result of the coin toss:', my_coin.get_sideup())

    print('coin toss simulation:')
    my_coin.toss()
    print('Result of the coin toss:', my_coin.get_sideup())

main()


