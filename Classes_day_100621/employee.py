class Employee:
    def __init__(self,surname,id):
        self.surname = surname
        self.id = id
    def set_surname(self,surname):
        self.surname = surname
    def get_surname(self):
        return self.surname
    def get_id(self):
        return self.id

class ProductionWorker(Employee):
    def __init__(self,surname,id,shift_n,hourly_r):
        Employee.__init__(self,surname,id)
        self.shift_number = shift_n
        self.hourly_rate = hourly_r
    def set_shift_n(self, shift_n):
        self.shift_n = shift_n
    def get_shift_n(self):
        return self.shift_number
    def get_hourly_r(self):
        return self.hourly_rate



