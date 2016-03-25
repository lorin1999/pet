from conf import IMG, PATH
import lib
from kivy_viewer import show

if __name__ == '__main__':
    lib.populate_image_folder(IMG.FOLDER, IMG.EXT, maxImages=25)
    show(lib.fetch_image_paths(PATH.IMAGES, IMG.EXT))
