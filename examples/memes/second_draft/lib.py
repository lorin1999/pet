"""
Helpers for image handling, fetching, manipulation, etc.

Ideas:
    * create thumbnails with Pillow
"""
import collections
import os
from glob import glob
import shutil
import sys

import requests
from slugify import slugify

from conf import IMG


class ImageHarvester(object):
    Info = collections.namedtuple('Info', ['path', 'content'])
    Info.__new__.__defaults__ = (None,) * len(Info._fields)

    def __init__(self, dstPath, ext, maxImages, refresh):
        self.dstPath = dstPath
        self.ext = ext
        self.maxImages = maxImages
        self.refresh = refresh

    def harvest(self):
        """Do the whole dance of preparing, fetching and saving images"""
        self.initialize_dst_path(self.refresh)
        memes = self.fetch_json()['data']['memes']
        self.download_images(memes)

    def initialize_dst_path(self, wipe=False):
        """Make sure the images folder is in the desired state.
        If the folder does not exist, it will be created.

        :param wipe: If `True` the folder will be deleted and recreated
        """
        if os.path.exists(self.dstPath):
            if not wipe:
                return

            # little sanity check (this is deleting data - be extra careful)
            assert 'memes', self.dstPath
            assert self.dstPath.endswith(IMG.FOLDER), self.dstPath
            shutil.rmtree(self.dstPath)
        os.makedirs(self.dstPath)

    @staticmethod
    def fetch_json():
        """ fetch json from imageFlip API (see: https://api.imgflip.com)"""
        requests.packages.urllib3.disable_warnings()
        url = 'https://api.imgflip.com/get_memes'
        response = requests.get(url, verify=False)
        return response.json()

    def download_images(self, memes):
        """Iterate through the meme data and download the images"""
        for idx, meme in enumerate(memes):
            if idx == self.maxImages:
                break

            print "download", meme
            info = self.fetch_image(meme['name'], meme['url'])
            if info.content:
                self.save_image(info.path, info.content)

    def fetch_image(self, name, url, refresh=False):
        filename = slugify(name) + self.ext
        path = os.path.join(self.dstPath, filename)
        if os.path.exists(path) and not refresh:
            return self.Info()

        return self.Info(path, requests.get(url).content)

    @staticmethod
    def save_image(path, content):
        with open(path, 'wb') as f:
            f.write(content)
        print "saved", path


def populate_image_folder(dstPath, ext, maxImages=sys.maxint, refresh=True):
    ImageHarvester(dstPath, ext, maxImages, refresh).harvest()


def fetch_image_paths(imagesPath, ext):
    pattern = os.path.join(imagesPath, '*' + ext)
    return glob(pattern)
