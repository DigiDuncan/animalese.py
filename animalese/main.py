from animalese.lib.speech import SpeechString


# def add_character(soundfile, n, newchar, offset):
#     character = newchar.upper()
#     if character in ENGLISH_LETTERS:
#         soundfile = soundfile.overlay(ENGLISH[character], position = n * offset)
#     if character == " ":
#         soundfile = soundfile.overlay(AudioSegment.empty(), position = n * (offset * SPACE_WIDTH))


def main():
    print("Input text:")
    text = input("> ")

    SpeechString(text).play()

    print("Done!")


if __name__ == "__main__":
    main()
