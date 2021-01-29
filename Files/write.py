    # 'w' means we can write to file
with open('./write.txt', 'w') as write_file:
    write_file.write('Hello there')
        # \n adds a line break
    write_file.write('\nI can write in Python')

    # 'a' amends a file without overwriting it
with open('./write.txt', 'a') as write_file:
    write_file.write(' & add to my writings later on')

quotes = [
    '\nNow, young Skywalker, you will die.',
    '\n\nYou were the chosen one! It was said that you would destroy the Sith, not join them. \nYou were to bring balance to the Force, not leave it in darkness.'
]

with open('./write.txt', 'a') as write_file:
    write_file.writelines(quotes)