# import pydub

from animalese import constants


def start():
    constants.load()


def main():
    start()

    print("Input text:")
    text = input("> ")

    for c in text:
        pass


if __name__ == "__main__":
    main()
