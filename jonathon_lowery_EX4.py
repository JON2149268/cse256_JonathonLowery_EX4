# Jonathon Lowery
# CIS256 Fall 2024
# EX 4

import random

# create predefined list of words for user to guess
words = ['attorney', 'good', 'evil', 'science', 'fiction', 'reading', 'rainbow', 'hospital', 'instrument', 'equipment', 'land', 'water', 'mountain', 'coding', 'shocked', 'nomination', 'resignation', 'president', 'america']

# generate a random word from the word list and prompt user to guess the word
# one letter at a time
word = random.choice(words)
print(f"Guess the word, one letter at a time.")

# set the limit of user guesses
guesses = ' '
turns = 15

# define game parameters to reveal letter guessed
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")

        else:
            print("_")
            failed += 1

    if failed == 0:
        print(f"Congratulations! You won the game!!")
        print(f"The word is: ", word)
        break

    print()
# Create count keeping for number of guesses    
    guess = input(f"Guess a character:")
    guesses += guess
    # return statement for incorrect guesses and when user runs out of guesses
    if guess not in word:
        turns -= 1
        print(f"Incorrect guess")
        print(f"You have", + turns, "more guesses.")
        if turns == 0:
            print(f"Sorry, you lost the game. Better luck next time.")

            
            
