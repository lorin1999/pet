from conf import IMG, PATH
import kivy_example
import lib


if __name__ == '__main__':
    lib.populate_image_folder(
        IMG.FOLDER, IMG.EXT, maxImages=1, refresh=True)
    kivy_example.show(lib.fetch_image_paths(PATH.IMAGES, IMG.EXT))
