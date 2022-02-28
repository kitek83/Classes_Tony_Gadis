class CellPhone:
    def __init__(self,manuf,model,price):
        self.manuf = manuf
        self.model = model
        self.price = price
    def set_manuf(self, manuf):
        self.manuf = manuf
    def set_model(self,model):
        self.model = model
    def self_price(self, price):
        self.price()

    def get_manuf(self):
        return self.manuf
    def get_model(self):
        return self.model
    def get_price(self):
        return self.price
