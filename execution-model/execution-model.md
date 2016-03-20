# How does Python execute?

Although two distinct stages in the execution of a Python program are often mentioned (compile time (or import time) and runtime) there is actually only one execution phase once the code is parsed and compiled.

## 1. Phase (no execution): syntax check and byte compilation

When running a Python script the execution works exactly as you would expect: The interpreter reads the file line by line and executes all statements one after the other. Imports cause the execution to descend into the imported module and pops back up, when it walked through the imported module if the interpreter encounter a `def` or `class` statement, a function or class object is created and bound to the global namespace of the containing module [example](http://goo.gl/kL4XB). 

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

* [execution model in Python documentation](https://docs.python.org/2/reference/executionmodel.html)
* [good article about execution model](https://jeffknupp.com/blog/2013/02/14/drastically-improve-your-python-understanding-pythons-execution-model/)
