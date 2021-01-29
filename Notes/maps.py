from random import shuffle

words = ['gears', 'effect', 'duty', 'swamp']
anagrams = []

def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)

for word in words:
    anagrams.append(jumble(word))
print(anagrams)

    # using simple map takes for loop from 3 lines to 1 line
print(list(map(jumble, words)))

    # or comprehension way
print( [ jumble(word) for word in words ] )