class Account:
    def __init__(self,acc_num,int_rate,bal):
        self.acc_num = acc_num
        self.int_rate = int_rate
        self.balance = bal
    def set_acc_num(self,acc_num):
        self.acc_num = acc_num
    def set_int_rate(self,int_rate):
        self.int_rate = int_rate
    def set_balance(self,bal):
        self.balance = bal

    def get_acc_num(self):
        return self.acc_num
    def get_int_rate(self):
        return self.int_rate
    def get_balance(self):
        return self.balance

class CD(Account):
    def __init__(self,acc_num,int_rate,bal,mat_date):
        Account.__init__(self,acc_num,int_rate,bal)
        self.mat_date = mat_date

    def set_maturity(self,mat_date):
        self.mat_date = mat_date
    def get_maturity(self):
        return self.mat_date

