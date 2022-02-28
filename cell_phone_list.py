import cellphone1
def main():
    phones = make_list()
    print('Here are data entered by You:')
    display_list(phones)

def make_list():
    phone_list = []
    file = open('phone.txt','a')
    for count in range(1,6):
        print('Cell phone nr:',count,':')
        man = input('Enter brand of manufacturer of the phone:')
        mod = input('Enter model of the phone:')
        price = input('Enter retail price of the phone:')

        phone = cellphone1.CellPhone(man, mod, price)
        phone_list.append(phone)
        file.write(str(phone_list))
    file.close()
    return phone_list
def display_list(phone_list):
    for item in phone_list:
        print(item.get_manuf())
        print(item.get_model())
        print(item.get_price())
        print()




main()