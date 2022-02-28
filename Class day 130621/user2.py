from User import User
class Admin(User):
    def __init__(self,name,phone,address,email,priviliges):
        super().__init__(name,phone,address,email)
        self.priviliges = priviliges
        self.priviliges = Priviliges('')
class Priviliges:
    def __init__(self,priviliges):
        self.priviliges = priviliges

    def get_priviliges(self):
        priviliges = ['add post', 'delete post', 'ban user', 'change post']
        print('Admin has the following priviliges:')
        for priv in priviliges:
            print('*', priv)