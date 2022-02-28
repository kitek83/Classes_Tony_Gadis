import car
def main():
    ca_r = car.Car('Audi','A4',1999)
    print(ca_r.descritption())
    print(ca_r.read_odometer())
    print(ca_r.update_odometer(30))
    print(ca_r.increment_odometer(15))
    el_car = car.ElectricCar('Tesla','model s',2019)
    print(el_car.descritption())
    el_car.battery.get_battery_size()
    el_car.battery.range_battery()




main()