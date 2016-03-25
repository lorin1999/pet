import logging

from setuptools import setup, find_packages

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('setup.py')

packages = find_packages()
log.debug("found packages: %s", packages)

setup(
    name='python-course',
    version='0.2.0-dev',
    description='Materials and tools for an introductory Python Course',
    url='https://github.com/obestwalter/python-course',
    author='Oliver Bestwalter',
    license='MIT',
    install_requires=[
        'flask',
        'ipython',
        'jupyter',
        'plumbum',
        'requests[security]',
        'slugify',
    ],
    packages=packages,
    entry_points={'console_scripts': ['pc-make = _tools.make:main']},
)
