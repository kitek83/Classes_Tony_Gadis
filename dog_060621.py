class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(f'{self.name} is seating now.')
    def roll_over(self):
        print(f'{self.name} is rolling over now.')

my_dog = Dog('Willy',6)
print(f'My dog name is: {my_dog.name}')
print(f'My dog age is: {my_dog.age}')
my_dog.sit()
my_dog.roll_over()