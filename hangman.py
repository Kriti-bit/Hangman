import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly choose a word from the list
    while '-' in word or ' ' in word:
        # If there is a space or - in the word, we select another word randomly from the list
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word to be guessed
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # letters the user has already guessed

    while len(word_letters) > 0:

        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have used these letters: ', ' '.join(used_letters))

        # what current word is (i.e. W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current Word: ',' '.join(word_list))

        # Getting user input
        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('You have already used that character. Please try again')

        else:
            print('Invalid character. Please try again')

if __name__ == '__main__':
    hangman()
