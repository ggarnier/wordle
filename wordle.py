from random import randint
import re
import sys


MAX_GUESSES = 6
WORD_LENGTH = 5
DICTIONARY = []
RIGHT_LETTER = "x"
WRONG_POSITION = "o"
WRONG_LETTER = "_"


def load_dictionary():
    global DICTIONARY
    DICTIONARY = []
    with open("word-list.txt") as f:
        while line := f.readline():
            word = line.strip()
            if len(word) == WORD_LENGTH:
                DICTIONARY.append(word.lower())


def test_word(chosen_word, guess):
    result = ""
    for i, letter in enumerate(guess):
        if letter == chosen_word[i]:
            answer = RIGHT_LETTER
        elif letter in chosen_word:
            answer = WRONG_POSITION
        else:
            answer = WRONG_LETTER
        result += answer
    return result


def get_word():
    word_pattern = rf"^[a-z]{{{WORD_LENGTH}}}$"
    while True:
        word = input().lower()
        if not re.match(word_pattern, word):
            print(f"Word should have {WORD_LENGTH} letters")
        elif word not in DICTIONARY:
            print("Word not in dictionary")
        else:
            return word


def run():
    chosen_word = DICTIONARY[randint(0, len(DICTIONARY)-1)]
    guess_count = 0

    while True:
        guess_count += 1
        print(f"\nGuess #{guess_count}")
        guess = get_word()

        result = test_word(chosen_word, guess)
        if result == WORD_LENGTH * RIGHT_LETTER:
            print(f"Correct! You're right after {guess_count} guesses")
            sys.exit(0)
        print(result)

        if guess_count == MAX_GUESSES:
            print(f"Fail! Word was {chosen_word}")
            sys.exit(1)


if __name__ == "__main__":
    load_dictionary()
    run()
