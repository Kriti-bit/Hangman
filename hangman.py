import random
from words import words


def get_valid_word(words):
    word = random.choice(words)  # randomly choose a word from the list
    while '-' in word or ' ' in word:
        # If there is a space or - in the word, we select another word randomly from the list
        word = random.choice(words)
    return word
