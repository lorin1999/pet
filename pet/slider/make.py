import logging

from pet.jupiter_slider.slides import generate_slides

from pet.conf import OUTPUT_PATH


def basic_config():
    logging.basicConfig(level=logging.DEBUG)
    if OUTPUT_PATH.exists():
        OUTPUT_PATH.delete()
    OUTPUT_PATH.mkdir()


def main():
    basic_config()
    generate_slides()
