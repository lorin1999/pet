"""
Create a Window containing a collection of manipulable images from a folder.
See https://kivy.org/docs/examples/gen__demo__pictures__main__py.html

Something else you could try:
    * https://kivy.org/docs/tutorials/pong.html
    * even more ... https://kivy.org/docs/gettingstarted/examples.html
"""
from random import randint

from kivy.app import App
from kivy.uix.scatter import Scatter

# Cython support in PyCharm exists already but is in its infancy
# https://www.jetbrains.com/help/pycharm/2016.1/cython-support.html
# noinspection PyUnresolvedReferences
from kivy.properties import StringProperty

from memes import lib
from memes.conf import PATH, IMG


class Picture(Scatter):
    source = StringProperty(None)


class PicturesApp(App):
    def __init__(self, imagePaths, **kwargs):
        super(PicturesApp, self).__init__(**kwargs)
        self.imagePaths = imagePaths

    def build(self):
        for path in self.imagePaths:
            picture = Picture(source=path, rotation=randint(-30, 30))
            self.root.add_widget(picture)


def main():
    # there was a bug here that didn't show until refactoring
    # The folder instead of the path is passed here.
    # In the scripts before it didn't matter, as they only worked, when
    # the current work directory was where the app was
    # now we have a command line tool and we need an absolute path here
    # lib.populate_image_folder(IMG.FOLDER, IMG.EXT, maxImages=25)
    lib.populate_image_folder(PATH.CACHE, IMG.EXT, maxImages=25)
    PicturesApp(lib.fetch_image_paths(PATH.CACHE, IMG.EXT)).run()

if __name__ == '__main__':
    main()
