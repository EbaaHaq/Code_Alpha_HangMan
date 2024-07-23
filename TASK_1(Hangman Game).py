print("TASK1: CodeAlpha_HangMan_game")

import random

def select_random_word(word_list):
    return random.choice(word_list)


def display_hangman(tries):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |   
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |   
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   
           |   
           |
        --------
        """,
        """
           ------
           |    |
           |    
           |   
           |   
           |
        --------
        """
    ]
    return stages[tries]


def hangman():
    word_list = ["python", "hangman", "challenge", "programming", "developer", "CodeAlpha", "Internship", "Welcome"]
    word = select_random_word(word_list).upper()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6

    print("Welcome to Hangman!")
    while len(word_letters) > 0 and tries > 0:
        print(display_hangman(tries))
        print(f"You have {tries} tries left.")
        guessed_word = [letter if letter in guessed_letters else "_" for letter in word]
        print("Current word: ", " ".join(guessed_word))

        guess = input("Guess a letter: ").upper()
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in word_letters:
            word_letters.remove(guess)
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            tries -= 1
            guessed_letters.add(guess)
            print("Wrong guess!")

    if tries == 0:
        print(display_hangman(tries))
        print(f"Sorry, you lost. The word was {word}.")
    else:
        print(f"Congratulations, you guessed the word {word}!")


hangman()
