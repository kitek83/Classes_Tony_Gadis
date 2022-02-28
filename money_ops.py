import bankaccount
def main():
    balance = float(input('Enter your amount of the balance:'))

    money = bankaccount.Bank(balance)

    pay = float(input('Enter amount of the money, which you earned during the month:'))
    money.deposit(pay)
    print('Your balance account is:', format(money.show(),'.2f'))
    print()
    print(money)

    cash = float(input('Enter the amount of the money, which you want to withdraw:'))
    money.withdraw(cash)
    print('Your balance account is:', money.show())
    print()
    print(money)
main()
