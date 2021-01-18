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