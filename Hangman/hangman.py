import random


def hangman():
    words = ['python', 'java', 'kotlin', 'javascript']
    random.seed()
    correct_word = random.choice(words)

    print('H A N G M A N')
    guess = input('Guess the word: ')

    print('You survived!' if guess == correct_word else 'You are hanged!')


hangman()
