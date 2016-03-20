# Imports

To better structure the code you can distribute it to different files. A Python file is called a module and a directory containing an `__init__.py` is called a package which serves as a container for a collection of modules. Packages can be nested to create hierarchical collections of packages and modules. Addressing a nested the module works like describing the path to it only that you use dots to separate the parts of the path.

For imports to work the root of the imports you want to make has to be in sys.path - there are a lot of ways how this can be accomplished. For now, I will just mention two:


[demo](src/imports.py)
