class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year
        self.speed = 0
    def accelerate(self):
        self.speed += 5
    def brake(self):
        self.speed -= 5
    def set_make(self, make):
        self.make = make
    def get_speed(self):
        return self.speed