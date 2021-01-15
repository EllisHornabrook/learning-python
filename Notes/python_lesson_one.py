### NUMBERS ###
numOne = 3 / 3
    # returns float
numTwo = 3 // 3
    # returns integer
numOne + numTwo
    # returns result of two values, does not change numOne value
numTwo += 20
    # changes original value, also -= /= etc


### STRINGS ###
str = 'Hello\', hi, howdy'
    # use \ to escape a character
len(str)
    # gets length of string


### LISTS ###
list = ['Lets', 'make', 'a', 'list', 2]
    # lists can hold both strings and integers
listTwo = ['add', 'to', 'list']
list + listTwo
    # returns joint lists
newList = list + listTwo
    # creates new list
list.append(15) 
    # adds to the end
list.pop() 
    # removes from the end
list.remove(2) 
    # removes first instance of value given
listOfLists = [list, listTwo, [1, 2, 3]]
    # create new list with lists
del(listOfLists[1][2])
    # deletes the third value in the second list (s)


### PRINTING DATA ###
name = input('Tell me your name ')
    # asks for user input
print('Hello', name)
    # prints to console

radius = input('Enter the radius of your circle (m): ')
area = 3.142 * int(radius)**2
    # int turns string in to number/integer
print('The area of your circle is:', area)
    # comma adds a space = ' '


### FORMATTING ###
num1 = 5.27394
num2 = 12.488873
print('num1 is {0} and num2 is {1}'.format(num1, num2))
    # {} uses the index position from format()
print('short num1 is {0:.3} & num2 shows more {1:.3f}'.format(num1, num2))
    # :.* targets the first 3 numbers --- :.*f targets float, first 3 after decimal point
print(f'num1 is {num1:.4} and num2 is {num2:.1f}')
    # using f-strings, simpler way of using .format()


### IF STATEMENTS IN PYTHON ###
checkMe = 36
if checkMe < 10:
    print("that's a small number")
elif checkMe > 100:
    # elif is the same as else if in JS
    print('way too many')
else:
    print('no matches')

animals = input('Do you like dogs? (y/n): ')
if animals == 'y':
    # == check if value is equal to, no === used
    print('me too')
else:
    print("oh, you're cat person")


### LOOPS IN PYTHON ###
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


### RANGES ###
for n in range(5):
    # range() creates list of numbers from 0 to number before specified
    n
for n in range(10,31,5):
    # lists from 10 to 30 in stages of 5
    n
for charNum in range(len(characters)):
    # len(*) returns the length of *
    print(charNum, characters[charNum])
    # charNum = index position, in this example


### FUNCTIONS IN PYTHON ###
def function(name = 'person', response = 'okay'):
    # def "function name"(parameter): is how to write a function --- default value of person & okay
    print(f'Hello {name}, this is my first function. I\'m glad to hear you think my code is {response}.')

userName = input('Enter your name: ')
userResponse = input('Describe my work in one word: ')

function(userName, userResponse)