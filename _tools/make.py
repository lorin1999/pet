import logging

from _tools.conf import OUTPUT_PATH
from .slides import generate_slides


def basic_config():
    logging.basicConfig(level=logging.DEBUG)
    if OUTPUT_PATH.exists():
        OUTPUT_PATH.delete()
    OUTPUT_PATH.mkdir()


def main():
    basic_config()
    generate_slides()
