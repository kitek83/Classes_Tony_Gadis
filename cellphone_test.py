import cellphone
def main():
    manu = input('Enter the brand of phone manufacturer: ')
    mod = input('Enter model of the phone:')
    price = float(input('Enter price of the phone:'))

    phone = cellphone.Cellphone(manu,mod,price)

    print('Phone manufacturer:',phone.get_manufact())
    print('Phonem model:', phone.get_model())
    print('Phone retail price:', phone.get_price())


main()