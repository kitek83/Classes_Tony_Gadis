class Name:
    def __init__(self,name,surname,address,age):
        self.name = name
        self.surname = surname
        self.address = address
        self.age = age
    def get_name(self):
        return self.name
    def get_surname(self):
        return self.surname
    def get_address(self):
        return self.address
    def get_age(self):
        return self.age
    def __str__(self):
        return 'name:' + self.name + \
                '\nsurname: ' + self.surname + \
                '\naddress: ' + self.address + \
                '\nage: ' + self.age + \
                '\n'

