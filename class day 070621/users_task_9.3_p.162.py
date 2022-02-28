class User:
    def __init__(self,name,phone,address,email):
        self.name = name
        self.phone = phone
        self.address = address
        self.email = email
        self.login_attempt = 5
    def name_n(self):
        print(f'Name: {self.name}')
    def phone_s(self):
        print(f'Phone: {self.phone}')
    def address_s(self):
        print(f'Address: {self.address}')
    def email_l(self):
        print(f'Email:{self.email}')
    def greet_user_g(self):
        print(f'Hello {self.name}')
    def increment_login(self):
        self.login_attempt += 1
        print(f'You logged in {self.login_attempt} times.')

    def reset_login_attempts(self):
        self.login_attempt = 0
        print(f'Login attempts= {self.login_attempt}')


user1 = User('Jack','455666','Arkonska 8','kw@wp.pl')
user1.name_n()
user1.phone_s()
user1.address_s()
user1.email_l()
user1.greet_user_g()
print()
user2 = User('Kris','556644','Finska 17','kk@wp.pl')
user2.name_n()
user2.phone_s()
user2.address_s()
user2.email_l()
user2.greet_user_g()
print('------------------------')
user3 = User('Alice','54445','Szwedzka8','jj@we.pl')
user3.increment_login()
user3.reset_login_attempts()
