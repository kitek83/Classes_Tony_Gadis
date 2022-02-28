import coin_class
my_coin = coin_class.Coin()
print('Result of the toss coin is:', my_coin.result())
print('Simulation of 10 tosses of the coin:')
for n in range(10):
    my_coin.toss()
    print(my_coin.result())

