import pickle
import cellphone
FILE_NAME = 'celphone.dat'
def main():
    again = 't'
    file = open(FILE_NAME, 'wb')
    while again.lower() == 't':

        man = input('Enter brand of manufacturer:')
        mod = input('Ente model of cell phone:')
        price = input('Enter retail price of the phone.')

        phone = cellphone.CellPhone(man, mod, price)
        pickle.dump(phone, file)
        again = input('Enter "t" if you want to add another cellphone or another mark to finish.')
    file.close()

main()