import random
class Coin:
    def __init__(self):
        self.__sideup = 'orzel'
    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = 'orzel'
        else:
            self.__sideup = 'reszka'
    def get_sideup(self):
        return self.__sideup
def main():
    my_coin = Coin()
    print('The result of toss coin:', my_coin.get_sideup())
    print('Inistializing simulation of one toss coin:')
    my_coin.toss()
    #my_coin.sideup = 'orzel'
    print('The result of toss coin is:',my_coin.get_sideup())
    print('Simulation of 10 toss coin')
    for n in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

main()