class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(f'{self.name} is siting now.')
    def roll_over(self):
        print(f'{self.name} is rolling over.')

my_dog = Dog('Azor', 5)
your_dog = Dog('Lucy', 3)

print(f'My dog name is {my_dog.name}')
print(f'My dog is {my_dog.age} years old.')
my_dog.sit()
my_dog.roll_over()
print()

print(f'Your dog name is {your_dog.name}.')
print(f'Your dog age is {your_dog.age}.')
your_dog.sit()
your_dog.roll_over()