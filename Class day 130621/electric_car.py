from car import Car

class Battery:
    def __init__(self, battery_size=100):
        self.battery_size = battery_size
    def get_battery_size(self):
        print(f'Battery size is {self.battery_size} kWh.')
    def range_battery(self):
        if self.battery_size == 75:
            range = 265
        elif self.battery_size == 100:
            range = 300
        print(f'Range of the el car is {range} miles on full charge.')

class ElectricCar(Car):
    def __init__(self,make,model,year):
       super().__init__(make,model,year)
       #creating an object in child class
       self.battery = Battery()