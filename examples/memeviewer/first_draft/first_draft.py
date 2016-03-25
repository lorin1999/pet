import os
from glob import glob
from random import randint
import shutil

from kivy.app import App
from kivy.uix.scatter import Scatter
# noinspection PyUnresolvedReferences
from kivy.properties import StringProperty
import requests
from slugify import slugify


requests.packages.urllib3.disable_warnings()


class Picture(Scatter):
    source = StringProperty(None)


class PicturesApp(App):
    def __init__(self, dstPath, ext, refresh=False, maxImages=1, **kwargs):
        super(PicturesApp, self).__init__(**kwargs)
        self.dstPath = dstPath
        self.ext = ext
        self.maxImages = maxImages
        self.pattern = os.path.join(dstPath, '*' + ext)
        if os.path.exists(self.dstPath):
            if not refresh:
                return

            # little sanity check (this deletes data - be extra careful)
            assert self.dstPath.endswith('images'), self.dstPath
            shutil.rmtree(dstPath)
        os.makedirs(self.dstPath)

    def build(self):
        url = 'https://api.imgflip.com/get_memes'
        page = requests.get(url, verify=False)
        memes = page.json()['data']['memes']
        for idx, meme in enumerate(memes):
            if idx == self.maxImages:
                break

            print "fetch", meme['url']
            ret = requests.get(meme['url'], stream=True)
            filename = slugify(meme['name']) + self.ext
            path = os.path.join(self.dstPath, filename)
            if os.path.exists(path):
                continue

            print "save", meme['url']
            with open(path, 'wb') as f:
                for chunk in ret.iter_content(512):
                    f.write(chunk)

        for path in glob(self.pattern):
            print "add path to widget", path
            picture = Picture(source=path, rotation=randint(-30, 30))
            self.root.add_widget(picture)

    def on_pause(self):
        return True


if __name__ == '__main__':
    PicturesApp('images', '.jpg', maxImages=10, refresh=True).run()
