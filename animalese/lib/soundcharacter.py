import importlib.resources as pkg_resources

from pydub import AudioSegment

from animalese.data.audio import english


class SoundCharacter:
    def __init__(self, c, sound, offset = 100):
        self.c = c
        self.sound = sound
        self.offset = offset


ENGLISH = {
    " ": SoundCharacter(" ", AudioSegment.empty(), offset = 250),
    "missingno": SoundCharacter("missingno", AudioSegment.empty())
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
            ENGLISH[filename] = SoundCharacter(filename, AudioSegment.from_file(wav_file, format = "wav"))


load()
