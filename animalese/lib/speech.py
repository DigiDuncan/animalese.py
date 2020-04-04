from functools import lru_cache
import importlib.resources as pkg_resources

from pydub import AudioSegment
from pydub.playback import play

from animalese.data.audio import english

DEFAULT_LENGTH = 75


class SpeechCharacter:
    def __init__(self, c, sound, offset = DEFAULT_LENGTH):
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
        outsound = AudioSegment.empty()
        for sc in self.scs:
            outsound += sc.sound[:DEFAULT_LENGTH]
        return outsound

    def play(self):
        play(self.audio)

    def save(self, path, **kwargs):
        if "format" not in kwargs:
            kwargs["format"] = "wav"
        self.audio.export(path, **kwargs)

    def __len__(self):
        return len(self.audio)


ENGLISH = {
    " ": SpeechCharacter(" ", AudioSegment.silent(duration = DEFAULT_LENGTH)),
    "missingno": SpeechCharacter("missingno", AudioSegment.silent(duration = DEFAULT_LENGTH))
}


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


load()
