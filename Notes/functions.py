def function(name = 'person', response = 'okay'):
    # def "function name"(parameter): is how to write a function --- default value of person & okay
    print(f'Hello {name}, this is my first function. I\'m glad to hear you think my code is {response}.')

userName = input('Enter your name: ')
userResponse = input('Describe my work in one word: ')

function(userName, userResponse)