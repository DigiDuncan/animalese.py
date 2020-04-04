from functools import lru_cache
import importlib.resources as pkg_resources

from pydub import AudioSegment
from pydub.playback import play

from animalese.data.audio import english

DEFAULT_LENGTH = 750


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
        outlength = len(self)
        outsound = AudioSegment.silent(duration = outlength)
        offset = 0
        for sc in self.scs:
            outsound += sc.sound[:DEFAULT_LENGTH]
            offset += sc.offset
        return outsound

    def play(self):
        play(self.audio)

    def save(self, path, **kwargs):
        if "format" not in kwargs:
            kwargs["format"] = "wav"
        self.audio.export(path, **kwargs)

    @lru_cache()
    def __len__(self):
        maxending = 0
        offset = 0
        for sc in self.scs:
            ending = offset + len(sc)
            maxending = max(ending, maxending)
            offset += sc.offset
        return maxending


ENGLISH = {
    " ": SpeechCharacter(" ", AudioSegment.empty()),
    "missingno": SpeechCharacter("missingno", AudioSegment.empty())
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
