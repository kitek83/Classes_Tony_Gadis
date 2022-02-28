#program showa passing object as an argument of the function
import coin
def main():
    my_coin = coin.Coin()
    print(my_coin.result())
    flip(my_coin)
    print(my_coin.result())

def flip(my_coin):
    my_coin.toss()
main()