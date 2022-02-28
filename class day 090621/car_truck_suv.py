import vehicles
def main():
    car = vehicles.Car('Volvo','V5',70000,15000,4)
    track = vehicles.Track('Jeep','Land',80000,25000,'4WD')
    suv = vehicles.SUV('Skoda','J5',67000,35000,5)

    print('There is following car in the offer:')
    print('brand: ', car.get_make())
    print('model: ',car.get_model())
    print('mileage: ',car.get_mileage())
    print('price: ', car.get_price())
    print('doors: ',car.get_doors())
    print()
    print('There is following off-road car in the offer:')
    print('brand: ', track.get_make())
    print('model: ', track.get_model())
    print('mileage',track.get_mileage())
    print('price',track.get_price())
    print('drive type',track.get_drive_type())
    print()
    print('There is following SUV car in the offer.')
    print('brand: ', suv.get_make())
    print('model: ', suv.get_model())
    print('mileage',suv.get_mileage())
    print('price', suv.get_price())
    print('passenger capacity: ', suv.get_pass_cap())


main()