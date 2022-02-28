class Contacts:
    def __init__(self,name,phone,email): #initializing attribute
        self.name = name
        self.phone = phone
        self.email = email
    #assigning attributes values
    def set_name(self,name):
        self.name = name
    def set_phone(self, phone):
        self.phone = phone
    def set_email(self,email):
        self.email = email
    #return attribute values
    def get_name(self):
        return self.name
    def get_phone(self):
        return self.phone
    def get_email(self):
        return self.email
    #information about the state of the object
    def __str__(self):
        return 'Name and surname: ' + self.name + \
            '\nPhone:' + self.phone +  \
            '\nEmail:' + self.email


