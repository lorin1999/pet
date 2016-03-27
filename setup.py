"""
pip install https://github.com/ipython-contrib/
IPython-notebook-extensions/archive/master.zip --user
"""
import logging
from setuptools import find_packages, setup

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('setup.py')

packages = find_packages()
log.debug("found packages: %s", packages)

setup(
    name='python-course',
    version='0.2.0.dev0',
    description='Materials and tools for an introductory Python Course',
    url='https://github.com/obestwalter/python-course',
    author='Oliver Bestwalter',
    license='MIT',
    install_requires=[
        'requests[security]',
        'plumbum',

        'jupyter',
        'nbpresent',
        'funcsigs',  # undocumented nbpresent dependency
    ],
    packages=packages,
    entry_points={'console_scripts': ['pc-make = _tools.make:main']},
)
