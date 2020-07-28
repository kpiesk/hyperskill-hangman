import random


def hangman():
    print('H A N G M A N')
    words = ['python', 'java', 'kotlin', 'javascript']
    random.seed()
    correct_word = random.choice(words)
    guess_letters(correct_word)


# allows the user to guess the letters 8 times
def guess_letters(correct_word):
    tries = 8
    user_word = ['-'] * len(correct_word)

    while tries > 0:
        print(f"\n{''.join(user_word)}")
        user_letter = input('Input a letter: ')

        # if the user guesses the letter correctly, that letter is uncovered
        if user_letter in correct_word:
            for i in range(len(correct_word)):
                if correct_word[i] == user_letter:
                    user_word[i] = user_letter
        else:
            print('No such letter in the word')
        tries -= 1

    print("\nThanks for playing!"
          "\nWe'll see how well you did in the next stage")


hangman()
