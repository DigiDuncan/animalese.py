from pydub import AudioSegment
from pydub.playback import play

from animalese.lib.speech import getSC, calclength


# def add_character(soundfile, n, newchar, offset):
#     character = newchar.upper()
#     if character in ENGLISH_LETTERS:
#         soundfile = soundfile.overlay(ENGLISH[character], position = n * offset)
#     if character == " ":
#         soundfile = soundfile.overlay(AudioSegment.empty(), position = n * (offset * SPACE_WIDTH))


def to_animalese(s):
    outlength = calclength(s)
    outsound = AudioSegment.silent(duration = outlength)
    offset = 0
    for c in s:
        sc = getSC(c)
        outsound = outsound.overlay(sc.sound, position = offset)
        offset += sc.offset

    return outsound


def main():
    print("Input text:")
    text = input("> ")

    outsound = to_animalese(text)

    play(outsound)
    print("Done!")


if __name__ == "__main__":
    main()
