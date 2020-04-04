import importlib.resources as pkg_resources

from animalese.data.audio import english
# from animalese.lib.utils import AttrDict


ENGLISH = None
JAPANESE = None


def load():
    global ENGLISH
    global JAPANESE

    english_dict = {}
    japanese_dict = {}

    for file in pkg_resources.contents(english):
        if file.endswith(".wav"):
            filename = file[:-4].upper()
            english_dict[filename] = pkg_resources.read_binary(english, file)

    ENGLISH = english_dict
    JAPANESE = japanese_dict

load()
