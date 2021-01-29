    # opens file
ipsum_file = open('./ipsum.txt')

    # reads through each line in text
for line in ipsum_file:
    print(line.rstrip())

    # seek moves cursor to character number entered
ipsum_file.seek(0)

    # readlines places each line in to a list as a string
lines = ipsum_file.readlines()

ipsum_file.seek(50)
    # reads 75 characters from the 50th character
file_text = ipsum_file.read(75)

    # closes file
ipsum_file.close()


def sequence_filter(line):
        # removes all lines with >
    return '>' not in line

    # with the text open do ...
with open('./text_sequence.txt') as text_file:
    lines = text_file.readlines()
    print(list(filter(sequence_filter, lines)))