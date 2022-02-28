import employee
def main():
    surn = input('Enter surname: ')
    id = input('Enter id: ')
    empl = employee.Employee(surn,id)

    shift_n = input('Enter shift number: ')
    hourly_r = input('Entewr hourly rate: ')
    prod = employee.ProductionWorker(shift_n,hourly_r)


    print('Surname:', empl.get_surname())
    print('Id: ', empl.get_id())
    print('Shift number: ', prod.get_shift_n())
    print('Hourly rate: ', prod.get_hourly_r())



main()