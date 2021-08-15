import random
from words import words
from hangman_visual import lives_visual_dict 
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
    lives = 7

    while len(word_letters) > 0 and lives > 0:

        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have ',lives,' lives left ','You have used these letters: ', ' '.join(used_letters))

        # what current word is (i.e. W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current Word: ',' '.join(word_list))

        # Getting user input
        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives = lives - 1 # takes away a life if the letter guessed is not in the word

        elif user_letter in used_letters:
            print('You have already used that character. Please try again')

        else:
            print('Invalid character. Please try again')

    if lives == 0:
        print(lives_visual_dict[lives])
        print('Sorry you died, the word was ', word)

    else:
        print('Congratulations! You guessed the word ',word,' correctly!!!')

if __name__ == '__main__':
    hangman()
