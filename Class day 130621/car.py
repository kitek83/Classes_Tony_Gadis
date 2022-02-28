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