class Pet:
    def __init__(self, name, type,age):
        self.name = name
        self.type = type
        self.age = age
    def name_a(self, name):
        self.name = name
    def type_a(self,type):
        self.type = type
    def age_a(self,age):
        self.age = age
    def get_name(self):
        return self.name
    def get_type(self):
        return self.type
    def get_age(self):
        return self.age

