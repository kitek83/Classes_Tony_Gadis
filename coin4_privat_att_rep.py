import random
class Coin:
    def __init__(self):
        self.__coin = 'orzel'
    def toss(self):
        if random.randint(0,1) == 0:
            self.__coin = 'orzel'
        else:
            self.__coin = 'reszka'
    def get_result(self):
        return self.__coin
def main():
    my_coin = Coin()
    print('This the result after toss coin:')
    print(my_coin.get_result())
    print('Simulation of 10 tosses of the coin')
    for tos in range(10):
        my_coin.toss()
        print('The result is:', my_coin.get_result())
main()
