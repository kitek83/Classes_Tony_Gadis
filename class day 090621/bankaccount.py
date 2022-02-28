class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
    def get_balance(self):
        return self.balance
