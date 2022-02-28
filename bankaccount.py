class Bank:
    def __init__(self,bal):
        self.balance = bal
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('You don\'t habe enough money.')
    def show(self):
        return self.balance
    def __str__(self):
        return 'Balance account is:' + format(self.balance, '.2f')



