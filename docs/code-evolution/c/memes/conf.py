import os


class IMG(object):
    FOLDER = 'meme-cache'
    EXT = '.jpg'


class PATH(object):
    ROOT = os.path.dirname(__file__)
    CONTENT = os.path.join(ROOT, '..', '..', '..', '..', 'docs')
    CACHE = os.path.join(ROOT, IMG.FOLDER)
