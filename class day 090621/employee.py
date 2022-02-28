class Employ:
    def __init__(self,id,name_surn,dep,pos):
        self.id = id
        self.name_surn = name_surn
        self.dep = dep
        self.pos = pos

    def get_id(self):
        return self.id
    def get_name_surn(self):
        return self.name_surn
    def get_dep(self):
        return self.dep
    def get_pos(self):
        return self.pos

    def __str__(self):
        return  '\n id:' + self.id + \
                'name&surname:' + self.name_surn + \
                '\n department: ' + self.dep + \
                '\n position:' + self.pos + \
                '\n'
