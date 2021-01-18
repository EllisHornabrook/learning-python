class Planet:
    def __init__(self, name, life, type):
        self.name = name
        self.life = life
        self.gravity = 'Yes'
            # can also be set in the class
        self.type = type

    def description(self):
        return f'{self.name} is a {self.type}'

mars = Planet('Mars', 'no', 'planet')
print(mars.description())


class Star_wars:

    fanbase = 'World-wide'
    owners = 'Disney'    
        # set data for class

    def __init__(self, lightsaber, name, side):
        self.lightsaber = lightsaber
        self.name = name
        self.side = side

    @classmethod
    def jedi_names(cls):
        return f'The company that own the rights to Star Wars are {cls.owners}'
        # cls targets data stored in the class

    @staticmethod
    def description(desc = 'collection of films'):
        # only takes in parameters you set (desc)
        return f'Star Wars is a {desc}'

print(Star_wars.jedi_names())