import pet
def main():
    name = input('Enter name of yout pet:')
    type = input('Enter type of your pet:')
    age = int(input('Enteer age of your pet:'))
    best_pet = pet.Pet(name,type,age)

    print(best_pet.get_name())
    print(best_pet.get_type())
    print(best_pet.get_age())

main()