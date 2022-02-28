import bankaccount
def main():
    balance = 2000
    my_acc = bankaccount.BankAccount(balance)

    pay = float(input('Enter earned money during the month:'))
    my_acc.deposit(pay)
    print(f'{pay} was added to your balance.')
    print('Your accouint balance is:', my_acc.get_balance())

    cash = float(input('Enter the amount of the money, you want to withdraw:'))
    my_acc.withdraw(cash)
    print(f'Your balance account is: {my_acc.get_balance()}')

main()