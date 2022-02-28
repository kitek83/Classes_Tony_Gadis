import pickle
import employee
LOOK_FOR = 1
ADD = 2
CHANGE =3
DELETE = 4
QUIT = 5
FILE_DAT = 'employee.dat'
def main():
    workers = load_file() #returning the list
    choice = 0
    while choice != QUIT:
        choice = menu()     #returning choice
        if choice == LOOK_FOR:
            look_for(workers)
        elif choice == ADD:
            add(workers)
        elif choice == CHANGE:
            change(workers)
        elif choice == DELETE:
            delete(workers)
    save_file(workers)
def load_file():
    try:
        file = open(FILE_DAT,'wb')
        workers = pickle.load(file)
    except IOError:
        workers = {}
    return workers

def menu():
    print('Menu:')
    print('1.Look for the worker.')
    print('2.Add new worker.')
    print('3.Change data for the worker.')
    print('4.Delete worker.')
    print('5.Quit the program.')
    choice = int(input('Enter nr from the menu'))
    while choice < LOOK_FOR or choice > QUIT:
        choice = input('Enter correct nr:')
    return choice

def look_for(workers):
    id = input('Enter id of the worker:')
    print(workers.get(id,'id was not found.'))

def add(workers):
    id = input('Enter id of the emplyee:')
    name = input('Enter the name:')
    dep = input('Enter department:')
    pos = input('Enter position:')
    if id not in workers:
        entry = employee.Employ(id,name,dep,pos)
        workers[id] = entry
    else:
        print('Name already exists.')

def change(workers):
    id = input('Enter id:')
    if id in workers:
        name = input('Enter the name:')
        dep = input('Enter department:')
        pos = input('Enter position:')
        entry = employee.Employ(id,name,dep,pos)
        workers[id] = entry
    else:
        print('Id was not found')

def delete(workers):
    id = input('Enter id of the emplyee')
    if id in workers:
        del workers[id]
    else:
        print('Id was not found.')

def save_file(workers):
    file = open(FILE_DAT, 'rb')
    pickle.dump(workers, file)
    file.close()

































main()
