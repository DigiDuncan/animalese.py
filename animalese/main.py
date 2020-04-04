from pydub import AudioSegment
from pydub.playback import play

from animalese.lib.constants import ENGLISH


def add_character(soundfile, n, newchar, offset):
    character = newchar.upper()
    if character in ENGLISH_LETTERS:
        soundfile = soundfile.overlay(ENGLISH[character], position = n * offset)
    if character == " ":
        soundfile = soundfile.overlay(AudioSegment.empty(), position = n * (offset * SPACE_WIDTH))


def calclength(text, offset):
    ends = [len(ENGLISH[c.upper()]) + offset * n for n, c in enumerate(text) if c.upper() in ENGLISH_LETTERS]
    maxend = max(ends)
    return maxend


def to_animalese(text):
    return AudioSegment.empty()


def main():
    print("Input text:")
    text = input("> ")

    outsound = to_animalese(text)

    play(outsound)
    print("Done!")


if __name__ == "__main__":
    main()
