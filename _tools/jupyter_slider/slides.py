import logging

from plumbum import local
# noinspection PyUnresolvedReferences
from plumbum.cmd import jupyter

from _tools.jupiter_slider.conf import PROJECT_PATH, OUTPUT_PATH

log = logging.getLogger(__name__)

BAD_FOLDER_NAMES = ['site-packages', '.ipynb_checkpoints']
"""Folder names that should be filtered from build"""

NO_EXECUTE_NOTEBOOKS = [
    'broken-syntax', 'undefined-names', 'easter-eggs', 'imports']
"""Notebooks that must not be executed as part of slide creation"""


def make_slides(path):
    # FIXME why does this not work? '--output=%s' % (OUTPUT_PATH)
    args = ['nbconvert', path, '--to=slides']
    if not any(name in path for name in NO_EXECUTE_NOTEBOOKS):
        args.append('--execute')
    # workaround: run converter directly in output folder
    with local.cwd(OUTPUT_PATH):
        jupyter(*args)


def filter_non_project_paths(p):
    return not any(name in p for name in BAD_FOLDER_NAMES)


def generate_slides():
    for path in sorted(PROJECT_PATH.walk(
            dir_filter=filter_non_project_paths,
            filter=lambda p: p.endswith('.ipynb'))):
        log.info('create slides from %s', path)
        make_slides(path)


if __name__ == '__main__':
    generate_slides()
