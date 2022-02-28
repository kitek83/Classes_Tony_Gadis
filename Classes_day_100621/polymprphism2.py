import animals
def main():
    mammal = animals.Mammamal('animal')
    dog = animals.Dog()
    cat = animals.Cat()

    show_info(mammal)
    print()
    show_info(dog)
    print()
    show_info(cat)
    print()
    show_info('This is text string.')

def show_info(creature):
    if isinstance(creature,animals.Mammamal):
        creature.show()
        creature.make_sound()
    else:
        print('It is not animal.')
main()