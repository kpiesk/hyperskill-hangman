import random


def hangman():
    print('H A N G M A N')
    words = ['python', 'java', 'kotlin', 'javascript']
    random.seed()
    correct_word = random.choice(words)
    guess_letters(correct_word)


# Allows the player to guess the word in 8 attempts
def guess_letters(correct_word):
    lives = 8  # lives are not lost if the guess is correct
    player_word = ['-'] * len(correct_word)

    while lives > 0:
        print(f"\n{''.join(player_word)}")
        # checks whether the user won the game
        if '-' not in player_word:
            print('You guessed the word!\nYou survived!')
            break
        player_letter = input('Input a letter: ')

        # checks whether the user has already attempted this letter
        if player_letter in correct_word and player_letter in player_word:
            print('No improvements')
            # player loses a life if attempts the already guessed letter
            lives -= 1

        # checks whether the user guessed the letter correctly
        elif player_letter in correct_word:
            for i in range(len(correct_word)):
                # all cases of the guessed letter is uncovered
                if correct_word[i] == player_letter:
                    player_word[i] = player_letter

        else:
            print('No such letter in the word')
            # player loses a life if their guess is incorrect
            lives -= 1

    else:
        print("You are hanged!")  # is only printed if the player lost


hangman()
