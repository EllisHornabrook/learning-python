### SCOPE ###
my_name = 'sille'

def print_local_name():
    my_name = 'Ell'
    # local scoped variable, does not affect global variable
    print('My name is', my_name)

def print_new_global_name():
    global my_name
    my_name = 'Ellis'
    # adding 'global (variable_name)' redefines global variable
    print('My name is', my_name)


### DICTIONARIES ###
hat_colours = {'red': 'Mario', 'green': 'Luigi', 'yellow': 'Wario'}
    # 'key': 'value' - target key to get value
hat_colours['green']
    # returns Luigi
'purple' in hat_colours
    # checks if 'key' is in the hat_colours dictionary - returns True/False
hat_colours.keys()
    # returns all keys in dictionary
hat_colours.values()
    # returns all values in dictionary
hat_colours['purple'] = 'Waluigi'
    # adds new ['key'] = 'with value'
no_hat = dict(name='Baby Bowser', age=4, hat='none')
    # create new dictionary

def character_intro(dict):
    for key, val in dict.items():
        print(f'I am {val} and my hat is {key}.')
character_intro(hat_colours)


### SORTING AND SETS ###
numbers = [3,6,2,87,3,6,0,9,8]
sorted(numbers)
    # sorts low to high, for strings > A-Z then a-z
set(numbers)
    # removes all duplicates from the list


### CLASSES ###
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


### METHODS ###
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