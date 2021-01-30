from words import word_list
import random

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    finished_word = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 6
    print("Let's play Hangman!")
    print(display_hangman(attempts))
    print(finished_word)
    print("\n")
    while not guessed and attempts > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(finished_word)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                finished_word = "".join(word_as_list)
                if "_" not in finished_word:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                finished_word = word
        else:
            print("Not a valid guess.")
        print(display_hangman(attempts))
        print(finished_word)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of attempts. The word was", word)

def display_hangman(attempts):
    stages = [
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
           ---
        """,
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     /
           ---
        """,
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     
           ---
        """,
        """
            --------
            |      |
            |      O
            |     \\|
            |      |
            |     
           ---
        """,
        """
            --------
            |      |
            |      O
            |      |
            |      |
            |     
           ---
        """,
        """
            --------
            |      |
            |      O
            |      
            |      
            |     
           ---
        """,
        """
            --------
            |      |
            |      
            |      
            |      
            |     
           ---
        """
    ]
    return stages[attempts]

def main():
    word = get_word()
    play(word)
    while input("Play again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()