class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(f'My dof {self.name} is sitting.')
    def roll_over(self):
        print(f'My dog {self.name} rolled over.')

my_dog = Dog('Willy', 6)
your_dog = Dog('Lucy', 3)

print(f'My dog name is {my_dog.name}.')
print(f'My dog age is {my_dog.age}.')
my_dog.sit()
my_dog.roll_over()
print()
print(f'Your dog name is {your_dog.name}.')
print(f'Your dog is {your_dog.age} years old.')
your_dog.sit()
your_dog.roll_over()