import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    user_letter = input("Guess a letter: ").upper()

    while len(word_letters) > 0:
        print("You have guessed the letters: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current Word: ", " ".join(word_list))

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in user_letter:
            print("You have already guessed that letter.")
        else:
            print("Invalid character")

user_input = input("Type something:")
print(user_input)

