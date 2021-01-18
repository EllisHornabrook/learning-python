characters = ['Harry Potter', 'Harley Quinn', 'Obi Wan', 'Jon Snow']
for character in characters:
    # for (each value) in (this list)
    if character == 'Harry Potter':
        character + ' is a Wizard'
    else:
        character

for character in characters[1:3]:
    # splice from [first to third, not including third]
    character

age = 24
years = 0
while years < age:
    if years == 0:
        years += 1
        continue
        # continue will go back to the start of the loop until the condition is met
    if years % 2 == 0:
        # check if years is an even nunber
        years
    years += 5