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

    # fixme not necessary
    def on_pause(self):
        return True


def show(imagePaths):
    PicturesApp(imagePaths).run()
