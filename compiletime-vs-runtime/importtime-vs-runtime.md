# How does Python execute?

[exection model](https://docs.python.org/2/reference/executionmodel.html)

There are two distinct stages in the execution of a Python program.

## Import time: syntax check and byte compilation

When running a Python script there is always one concrete entry point from where on the code parsed and byte compiled. The parsing always starts on the first line of the file that contains the entry point and descends into imported modules. If the syntax of any line of code is incorrect the execution is stopped immediately. Due to the dynamic nature of Python less problems are caught during compile time than in e.g. Java

demos:

* [function syntax](broken-syntax-in-function.py)
* [module syntax](broken-syntax-in-module.py)

## Runtime: code execution

after all used modules are imported and byte compiled, the code is executed.

demos:

* [undefined in module](undefined-name-in-module.py)
* [undefined in module](undefined-name-in-function.py)
