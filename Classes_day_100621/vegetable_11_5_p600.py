class Vegetable:
    def __init__(self,vegtype):
        self.vegtype = vegtype
    def message(self):
        print('This is vegetable.')
class Potato:
    def __init__(self):
        Vegetable.__init__(self,'tomato')
    def message(self):
        print('This is tomato.')

v = Vegetable('jarzyna')
p = Potato()

v.message()
p.message()