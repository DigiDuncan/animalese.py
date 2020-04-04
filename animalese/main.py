from animalese.lib.speech import SpeechString


def main():
    print("Input text:")
    text = input("> ")

    SpeechString(text).play()

    print("Done!")


if __name__ == "__main__":
    main()
