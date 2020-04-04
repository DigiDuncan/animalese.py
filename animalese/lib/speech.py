from functools import lru_cache
import importlib.resources as pkg_resources

from pydub import AudioSegment
from pydub.playback import play

from animalese.data.audio import english

DEFAULT_LENGTH = 75
SPACE_LENGTH = DEFAULT_LENGTH * 0.5
PUNC_LENGTH = DEFAULT_LENGTH * 1.5


class SpeechCharacter:
    def __init__(self, c, sound, offset = DEFAULT_LENGTH, **kwargs):
        self.c = c
        self.sound = sound
        self.offset = offset

    def __len__(self):
        return len(self.sound)


class SpeechString:
    def __init__(self, s):
        self.s = s
        self.scs = [getSC(c) for c in s]

    @property
    @lru_cache()
    def audio(self):
        outsound = AudioSegment.silent(duration = len(self))
        currentchar = 1
        for sc in self.scs:
            outsound = outsound.overlay(
                sc.sound.fade(start = DEFAULT_LENGTH, duration = 5, to_gain = -12.0), position = 75 * currentchar
            )
            currentchar += 1
        return outsound

    def play(self):
        play(self.audio)

    def save(self, path, **kwargs):
        if "format" not in kwargs:
            kwargs["format"] = "wav"
        self.audio.export(path, **kwargs)

    def __len__(self):
        return len(self.scs) * DEFAULT_LENGTH + DEFAULT_LENGTH


SPECIAL_CHARACTERS = {
    "missingno": {"duration": DEFAULT_LENGTH},
    " ": {"duration": SPACE_LENGTH},
    ".": {"duration": PUNC_LENGTH},
    "!": {"duration": PUNC_LENGTH, "word_volume": 125},
    "?": {"duration": PUNC_LENGTH, "word_pitch": 125}
}

ENGLISH = {}


def getSC(c):
    c = c.upper()
    return ENGLISH.get(c, ENGLISH["missingno"])


def load():
    global ENGLISH

    for file in pkg_resources.contents(english):
        if file.endswith(".wav"):
            filename = file[:-4].upper()
            wav_file = pkg_resources.open_binary(english, file)
            ENGLISH[filename] = SpeechCharacter(filename, AudioSegment.from_file(wav_file, format = "wav"))

    for c, d in SPECIAL_CHARACTERS.items():
        ENGLISH[c] = SpeechCharacter(c, AudioSegment.silent(duration = d["duration"]))


load()
