from conf import IMAGE, PATH
import kivy_example
import lib


if __name__ == '__main__':
    lib.populate_image_folder(
        IMAGE.FOLDER, IMAGE.EXT, maxImages=1, refresh=True)
    kivy_example.show(lib.fetch_image_paths(PATH.IMAGES, IMAGE.EXT))
