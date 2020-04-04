from animalese.lib.speech import SpeechString


def main():
    print("Input text:")
    text = input("> ")

    SpeechString(text).play()
    SpeechString(text).save("./out.wav")

    print("Done!")


if __name__ == "__main__":
    main()
