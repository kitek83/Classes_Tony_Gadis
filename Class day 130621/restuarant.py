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
