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