import pickle
import cellphone
FILE_N = 'celphone.dat'
def main():
    end_of_file = False
    file = open(FILE_N, 'rb')
    while not end_of_file:
        try:
            phone = pickle.load(file)
            display(phone)
        except EOFError:
            end_of_file = True
    file.close()
def display(phone):
    print('Manufacturer:',phone.get_manuf())
    print('Model:',phone.get_mod())
    print('Price:', phone.get_price())
    print()


main()