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
