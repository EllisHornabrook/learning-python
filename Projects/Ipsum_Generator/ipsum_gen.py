from random import randint

colours = ['BLUE', 'CYAN', 'PINK', 'WHITE', 'YELLOW', 'GREEN', 'RED', 'BLACK']

def add_colours(word):
    random_position = randint(0, len(colours) - 1)
    return f'{word} {colours[random_position]}'

paragraphs = int(input('How many paragraphs of my ipsum: '))

with open('./lorem.txt') as ipsum_original:
    items = ipsum_original.read().split()

    for n in range(paragraphs):
        colour_text = list(map(add_colours, items))
        with open('./colour_lorem.txt', 'a') as ipsum_colour:
            ipsum_colour.write(''.join(colour_text) + '\n\n')