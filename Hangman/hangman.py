from random import choice
from string import ascii_lowercase
from typing import List


# Allows the player to play the game Hangman
def hangman():
    words = ['python', 'java', 'kotlin', 'javascript']
    print('H A N G M A N')

    while True:
        game_choice = input('Type "play" to play the game, "exit" to quit: ')
        if game_choice == 'exit':
            break
        elif game_choice == 'play':
            word = choice(words)
            guess_letters(word)
        else:
            continue


# Allows the player to guess the letters of the randomly chosen word
def guess_letters(word):
    lives = 8
    hint: List[str] = ['-'] * len(word)
    guesses = set()

    while lives > 0:
        print(f"\n{''.join(hint)}")
        # checks whether the user won the game
        if '-' not in hint:
            print('You guessed the word!\nYou survived!\n')
            break
        guess = input('Input a letter: ')

        # checks whether the player entered exactly one letter
        if len(guess) != 1:
            print('You should input a single letter')
            continue
        # checks whether the player entered an English lowercase letter
        elif guess not in ascii_lowercase:
            print('It is not an ASCII lowercase letter')
            continue
        # checks whether the player has already attempted this letter
        elif guess in guesses:
            print('You already typed this letter')
        # checks whether the player guessed the letter correctly
        elif guess in word:
            # all cases of the guessed letter are uncovered
            hint = [guess if word[i] == guess else hint[i]
                    for i in range(len(word))]
        # checks whether the player guessed the letter incorrectly
        else:
            print('No such letter in the word')
            lives -= 1  # player loses a life if their guess is incorrect

        guesses.add(guess)

    else:
        print('You are hanged!\n')  # is only printed if the player lost


hangman()
