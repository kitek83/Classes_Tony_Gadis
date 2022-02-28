# a class, that can be used to represent the car
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_r = 0
    def descritption(self):
        long_name = f'{self.make} {self.model} {self.year}'
        return long_name

    def read_odometer(self):
        d = f'Mileage of this car: {self.odometer_r}'
        return d
    def update_odometer(self,mileage):
        if mileage >= self.odometer_r:
            self.odometer_r = mileage
        else:
            print('You can\'t roll back the odometer!')
        return 'The mileage of the car is: ' + str(self.odometer_r)
    def increment_odometer(self, miles):
        self.odometer_r += miles
        return 'Mileage after increment is ' + str(self.odometer_r)

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




































