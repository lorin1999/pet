import os


class IMG(object):
    FOLDER = 'meme-cache'
    EXT = '.jpg'


class PATH(object):
    ROOT = os.path.dirname(__file__)
    CACHE = os.path.join(ROOT, IMG.FOLDER)
