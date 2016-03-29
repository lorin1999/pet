"""
pip install https://github.com/ipython-contrib/
IPython-notebook-extensions/archive/master.zip --user
"""
import logging

from setuptools import find_packages, setup

# setup.py is a normal Python script
# If you have trouble, you can log variables to understand what's going on
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('setup.py')

packages = find_packages()
log.debug("find_packages() -> %s", packages)

setup(
    name='python-exploration-toolkit',
    version='0.2.0.dev0',
    url='https://github.com/obestwalter/python-course',
    author='Oliver Bestwalter',
    license='MIT',
    install_requires=[
        'howdoi',  # get answers from stackoverflow
        'plumbum',  # paths, file handling, cli and other nice things
        'requests[security]',  # access the web

        'jupyter[all]',  # interactive notebooks in the browser
        'nbpresent',  # presentation with jupyter
        'funcsigs',  # undocumented nbpresent dependency
    ],
    packages=packages,
    entry_points={'console_scripts': ['pc-make = _tools.make:main']},
)
