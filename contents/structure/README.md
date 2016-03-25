# Structuring larger programs

## Overview

**TODO**

build up

* the line as the most simple meaningful level of organization
* The block as the next step up
* functions and data
* classes as collection of functions and data
* modules (mostly just a file) as collection of all of the above
* package as collection of modules
* hierarchical tree of packages
* installable libraries and applications

#############

To better structure the code you can distribute it to different files. A Python file is called **module** and a directory containing an `__init__.py` is called **package** which serves as container for collections of modules. Packages can be nested to create hierarchical collections of packages and modules. Addressing a nested module works like describing the path to it only that you use dots to separate the parts of the path.


## Warning: importing is usually easy but it's hard

http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html

For imports to work, the root of the imports you want to make has to be in sys.path - there are a lot of ways how this can be accomplished, but they all have the same result: the path to the folder containing the root of your imports is in `sys.path` and therefore your packages and modules can be found. This can be accomplished by creating an installable package or simply by adding the path to `sys.path` before the imports. There are many ways. 

PyCharm gives the option to mark folders in the projects as source root (In project view right click on folder and choose "mark directory as sources root") which leads to that folder being in sys.path if a script is started inside PyCharm.


# Imports Structure


[demo](src/imports.ipynb)
