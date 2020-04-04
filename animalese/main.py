from pydub import AudioSegment
from pydub.playback import play

from animalese.lib.soundcharacter import getSC


# def add_character(soundfile, n, newchar, offset):
#     character = newchar.upper()
#     if character in ENGLISH_LETTERS:
#         soundfile = soundfile.overlay(ENGLISH[character], position = n * offset)
#     if character == " ":
#         soundfile = soundfile.overlay(AudioSegment.empty(), position = n * (offset * SPACE_WIDTH))


def calclength(text):
    maxending = 0
    offset = 0
    for c in text:
        sc = getSC(c)
        ending = offset + len(sc)
        maxending = max(ending, maxending)
        offset += sc.offset
    return maxending


def to_animalese(text):
    outlength = calclength(text)
    outsound = AudioSegment.silent(duration = outlength)
    offset = 0
    for c in text:
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
