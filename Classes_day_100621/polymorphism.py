import animals
def main():
    animal = animals.Mammamal('animal')
    cat = animals.Cat()
    dog = animals.Dog()

    info_animals(animal)
    print()
    info_animals(cat)
    print()
    info_animals(dog)
    print()
    

def info_animals(creature):
    creature.show()
    creature.make_sound()
main()