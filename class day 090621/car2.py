import vehicles
def main():
    used_car = vehicles.Car('Audi','A4',30000,1500,4)
    print('Brand: ',used_car.get_make())
    print('Model: ', used_car.get_model())
    print('Mileage: ',used_car.get_mileage())
    print('Price:', used_car.get_price())
    print('Doors: ', used_car.get_doors())
main()