import car

car_r = car.Car('','')
for n in range(5):
    car_r.accelerate()
    print(car_r.get_speed())
print('-----------------------------')
for x in range(5):
    car_r.brake()
    print(car_r.get_speed())