class CellPhone:
    def __init__(self, manuf, mod,price):
        self.manuf = manuf
        self.mod = mod
        self.price = price
    def manuf(self,manuf):
        self.manuf = manuf
    def mod(self, mod):
        self.mod = mod
    def price(self, price):
        self.price = price

    def get_manuf(self):
        return self.manuf
    def get_mod(self):
        return self.mod
    def get_price(self):
        return self.price

