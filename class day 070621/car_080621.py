class Car:
    def __init__(self, make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    def describe_car(self):
        print('Car data:')
        print(f'{self.make} {self.model} {self.year}')
    def read_odometer(self):
        print(f'This car has {self.odometer} miles on it.')
    def update_odometer(self,milage):
        if milage >= self.odometer:
            self.odometer = milage
        else:
            print('You can\'t roll back odometer.')
    def increment_odometer(self, milage):
        self.odometer += milage

my_car = Car('Adi','A4',2015)
my_car.describe_car()
my_car.read_odometer()

my_car.odometer = 25

my_car.read_odometer()
my_car.update_odometer(100)
my_car.read_odometer()
print('----------------------')

my_used_car1 = Car('Peguot', '407SW',2008)
print(my_used_car1.describe_car())

my_used_car1.update_odometer(2500)
print(my_used_car1.read_odometer())

my_used_car1.increment_odometer(500)
print(my_used_car1.read_odometer())