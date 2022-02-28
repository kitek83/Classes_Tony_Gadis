class Mammamal:
    def __init__(self, species):
        self.species = species
    def show(self):
        print('This is ' + self.species)
    def make_sound(self):
        print('Grrrrr')

class Dog(Mammamal):
    def __init__(self):
        Mammamal.__init__(self,'dog')
    def make_sound(self):
        print('Hau, hau!')

class Cat(Mammamal):
    def __init__(self):
        Mammamal.__init__(self,'cat')
    def make_sound(self):
        print('Miau')
