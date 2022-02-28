class Teddy:
    quantity = 200
    size = 5

    def __init__(self,name,color):
        self.name = name
        self.color = color

    def change_color(self, color):
        print('This is a method.')
        self.color = color
    def change_name(self, name):
        print('changing the name.')
        self.name = name

teddy1 = Teddy('Ted', 'red')
print(teddy1.name)
print(teddy1.color)

teddy1.change_color('orange')
print(teddy1.name)
print(teddy1.color)

teddy1.change_name('Roby')
print(teddy1.name)
