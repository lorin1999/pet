import lib
from conf import IMG, PATH
from kivy_viewer import show


def main():
    # there was a bug here that didn't show until refactoring
    # The folder instead of the path is passed here.
    # In the scripts before it didn't matter, as they only worked, when
    # the current work directory was where the app was
    # now we have a command line tool and we need an absolute path here
    # lib.populate_image_folder(IMG.FOLDER, IMG.EXT, maxImages=25)
    lib.populate_image_folder(PATH.CACHE, IMG.EXT, maxImages=25)
    show(lib.fetch_image_paths(PATH.CACHE, IMG.EXT))

if __name__ == '__main__':
    main()
