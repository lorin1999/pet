import logging

from plumbum import LocalPath
# noinspection PyUnresolvedReferences
from plumbum.cmd import jupyter

log = logging.getLogger(__name__)

BAD_FOLDER_NAMES = ['site-packages', '.ipynb_checkpoints']
"""Folder names that should be filtered from build"""

NO_EXECUTE_NOTEBOOKS = [
    'broken-syntax', 'undefined-names', 'easter-eggs', 'imports']
"""Notebooks that must not be executed as part of slide creation"""


def make_slides(path):
    args = ['nbconvert', path, '--to=slides']
    if not any(name in path for name in NO_EXECUTE_NOTEBOOKS):
        args.append('--execute')
    # if you want to use stdlib tools, you can use the subprocess module
    jupyter(*args)


def filter_non_project_paths(p):
    return not any(name in p for name in BAD_FOLDER_NAMES)


def main():
    projectPath = LocalPath(__file__).dirname.up()
    """:type: LocalPath"""
    for path in sorted(projectPath.walk(
            dir_filter=filter_non_project_paths,
            filter=lambda p: p.endswith('.ipynb'))):
        log.info('create slides from %s', path)
        make_slides(path)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
