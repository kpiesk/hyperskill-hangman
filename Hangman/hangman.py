import random


def hangman():
    words = ['python', 'java', 'kotlin', 'javascript']
    random.seed()
    correct_word = random.choice(words)
    help_word = correct_word[:3] + '-' * (len(correct_word) - 3)

    print('H A N G M A N')
    user_guess = input(f'Guess the word: {help_word}')
    print('You survived!' if user_guess == correct_word
          else 'You are hanged!')


hangman()
