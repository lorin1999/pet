import os


class IMAGE(object):
    FOLDER = 'images'
    EXT = '.jpg'


class PATH(object):
    ROOT = os.path.dirname(__file__)
    IMAGES = os.path.join(ROOT, IMAGE.FOLDER)
