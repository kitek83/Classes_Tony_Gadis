class Restaurant:
    def __init__(self, rest_name, cuisine_type):
        self.rest_name = rest_name
        self.cuisine_type = cuisine_type
        self.number_surved = 0
    def describe_restaurant(self):
        print(f'Restaurant name is {self.rest_name}')
        print(f'Cusisine type offered is {self.cuisine_type} ')
    def open_restaurant(self):
        print(f'{self.rest_name} is open.')


    def surved_customers(self,customer):
        self.number_surved += customer
        print(f'Restaurant has served {self.number_surved} customers.')

    def increment_number_surved(self,add_customer):
        self.number_surved += add_customer
        print(f'Restauran during this day has served {add_customer} customers.')
        print(f'Restaurant totally served {self.number_surved} customers.')
my_rest = Restaurant('Felix', 'Chinese cuisine.')
my_rest2 = Restaurant('Chata', 'Polish cuisine.')
my_rest3 = Restaurant('Pedro','Mexican cuisine.')

my_rest.describe_restaurant()
print()
my_rest2.describe_restaurant()
print()
my_rest3.describe_restaurant()
print()
my_rest.open_restaurant()
print('----------------------')

restaurant = Restaurant('Alex','German cuisine.')
restaurant.surved_customers(25)
restaurant.increment_number_surved(5)

class IceCreanStand(Restaurant):
    def __init__(self,rest_name, cusine_type,flavors):
        super().__init__(rest_name,cusine_type)
        self.flavors = flavors


    def get_flavors(self):
        flavors = ['chocolate', 'vanilla', 'strawbery', 'cherry', 'rum', 'pistachio']
        print(f'The restaurans has following icecream flavors: {flavors}')
ice = IceCreanStand('','','') # '' - this is an empty argument; I passed 3 empty missing arguments
print('--------------------')
ice.get_flavors()























