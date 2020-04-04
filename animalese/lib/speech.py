import importlib.resources as pkg_resources

from pydub import AudioSegment

from animalese.data.audio import english

DEFAULT_OFFSET = 80
SPACE_OFFSET = 100


class SpeechCharacter:
    def __init__(self, c, sound, offset = DEFAULT_OFFSET):
        self.c = c
        self.sound = sound
        self.offset = offset

    def __len__(self):
        return len(self.sound)


class SpeechString:
    def __init__(self, s):
        self.scs = [getSC(c) for c in s]


ENGLISH = {
    " ": SpeechCharacter(" ", AudioSegment.empty(), offset = SPACE_OFFSET),
    "missingno": SpeechCharacter("missingno", AudioSegment.empty())
}


def getSC(c):
    c = c.upper()
    return ENGLISH.get(c, ENGLISH["missingno"])


def calclength(text):
    maxending = 0
    offset = 0
    for c in text:
        sc = getSC(c)
        ending = offset + len(sc)
        maxending = max(ending, maxending)
        offset += sc.offset
    return maxending


def load():
    global ENGLISH

    for file in pkg_resources.contents(english):
        if file.endswith(".wav"):
            filename = file[:-4].upper()
            wav_file = pkg_resources.open_binary(english, file)
            ENGLISH[filename] = SpeechCharacter(filename, AudioSegment.from_file(wav_file, format = "wav"))


load()
