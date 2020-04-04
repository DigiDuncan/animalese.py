# import pydub

from animalese.lib import constants
from animalese.lib.constants import ENGLISH


def main():
    print("Input text:")
    text = input("> ")

    for c in text:
        letter = c.upper()
        print(ENGLISH[letter])


if __name__ == "__main__":
    main()
