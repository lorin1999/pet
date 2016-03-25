import lib
from conf import IMG, PATH
from kivy_viewer import show


if __name__ == '__main__':
    lib.populate_image_folder(IMG.FOLDER, IMG.EXT, maxImages=25)
    show(lib.fetch_image_paths(PATH.CACHE, IMG.EXT))
