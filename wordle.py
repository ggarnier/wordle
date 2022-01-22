import argparse
from random import randint
import re
import sys


MAX_GUESSES = 6
WORD_LENGTH = 5
DICTIONARY = []
RIGHT_LETTER = "x"
WRONG_POSITION = "o"
WRONG_LETTER = "_"
WORD_PATTERN = re.compile(rf"^[a-z]{{{WORD_LENGTH}}}$")


def cleanup_word(line):
    word = line.strip().lower()
    if WORD_PATTERN.match(word):
        return word
    return ""


def load_dictionary(filepath):
    global DICTIONARY
    DICTIONARY = []
    with open(filepath) as f:
        while line := f.readline():
            word = cleanup_word(line)
            if len(word) == WORD_LENGTH:
                DICTIONARY.append(word.lower())

    if len(DICTIONARY) == 0:
        print("Dictionary is empty")
        sys.exit(1)
    print(f"Dictionary contains {len(DICTIONARY)} words")


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
    while True:
        word = input().lower()
        if not WORD_PATTERN.match(word):
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
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dictionary", required=True, help="path to the dictionary file")
    args = parser.parse_args()
    load_dictionary(args.dictionary)
    run()
