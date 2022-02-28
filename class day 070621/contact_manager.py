import pickle
import contact
LOOK_FOR = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
FILE_NAME = 'contacts.dat'

def main():
    contacts = load_cont()
    choice = 0
    while choice != QUIT:
        choice = menu()
        if choice == LOOK_FOR:
            look_for(contacts)
        if choice == ADD:
            add(contacts)
        if choice == CHANGE:
            change(contacts)
        if choice == DELETE:
            delete(contacts)
    save_file(contacts)
def load_cont():
    try:
        file = open(FILE_NAME, 'wb')
        contacts = pickle.load(FILE_NAME)
    except:
        contacts = {}
    return contacts
def menu():
    print()
    print('Menu.')
    print('1.Enter the name to look for the data.')
    print('2.Add data.')
    print('3.Change existing data')
    print('4.Delete the contact entry')
    print('5.Quit.')
    choice = int(input('Enter number from the menu:'))
    while choice < LOOK_FOR or choice > QUIT:
        choice = input('Enter correct nr from the menu:')
    return choice
def look_for(contacts):
    name = input('Enter 1st and 2nd name:')
    print(contacts.get(name,'Name was not found.'))

def add(contacts):
    name = input('Enter 1st and 2nd name:')
    phone = input('Enter phone number:')
    email = input('Enter email address:')

    if name not in contacts:
        entry = contact.Contacts(name, phone, email)
        contacts[name] = entry
    else:
        print('Name already exist.')
def change(contacts):
    name = input('Enter 1st and 2nd name:')
    if name in contacts:
        phone = input('Enter correct phone nr:')
        email = input('Enter correct email address:')
        entry = contact.Contacts(name,phone,email)
        contacts[name] = entry
    else:
        print('Name wasn\'t found.')
def delete(contacts):
    name = input('Enter 1st and 2nd name:')
    if name in contacts:
        del contacts[name]
    else:
        print('Name was not found')
def save_file(contacts):
    file = open(FILE_NAME, 'wb')
    pickle.dump(contacts,file)
    file.close()





































main()