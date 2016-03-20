# How does Python execute?

Although two distinct stages in the execution of a Python program are often mentioned (compile time (or import time) and runtime) there is actually only one execution phase once the code is parsed and compiled.

## 1. Phase (no execution): syntax check and byte compilation

When running a Python script there is always one concrete entry point from where on the code parsed and byte compiled. The parsing always starts on the first line of the file that contains the entry point and descends into imported modules. If the syntax of any line of code is incorrect the execution is stopped immediately. Due to the dynamic nature of Python less problems are caught during compile time than in e.g. Java

demos:

* [function syntax](broken-syntax-in-function.py)
* [module syntax](broken-syntax-in-module.py)

## 2. Phase: code execution

after all used modules are imported and byte compiled, the code is executed.

**IMPORTANT:** the definition of classes and functions are normal statements which are executed, the moment they are encountered by the interpreter. The results are objects in the active scope.

demos:

* [undefined in module](undefined-name-in-module.py)
* [undefined in module](undefined-name-in-function.py)

## Resources

[execution model in Python documentation](https://docs.python.org/2/reference/executionmodel.html)
