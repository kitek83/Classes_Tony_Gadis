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
