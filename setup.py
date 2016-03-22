from setuptools import setup

setup(
    name='python-course',
    version='0.2.0-dev',
    description='Materials and tools for an introductory Python Course',
    url='https://github.com/obestwalter/python-course',
    author='Oliver Bestwalter',
    license='MIT',
    install_requires=[
        'ipython',
        'jupyter',
        'requests',
        'plumbum',
    ],
    packages=['_tools'],
    entry_points={'console_scripts': ['pc-make = _tools.make:main']},
)
