# How does Python execute?

Although two distinct stages in the execution of a Python program are often mentioned (compile time (or import time) and runtime) there is actually only one execution.

## Execution (just one phase - nothing fancy)

When running a Python script the execution works exactly as you would expect: The interpreter reads the file line by line and executes all statements one after the other. Imports cause the execution to descend into the imported module and pops back up, when it walked through the imported module if the interpreter encounter a `def` or `class` statement, a function or class object is created and bound to the global namespace of the containing module. **To make it absolutely clear:** the definition of classes and functions are normal statements which are executed the moment they are encountered by the interpreter. The result of the execution of those statements are the creation of objects that are bound to the current namespace (in this case the module namespace) [example](http://goo.gl/jluF7F); [example with syntax errors](broken-syntax.ipynb); [example with undefined names](undefined-names.ipynb).

## Resources

* [execution model in Python documentation](https://docs.python.org/2/reference/executionmodel.html)
* [good article about execution model](https://jeffknupp.com/blog/2013/02/14/drastically-improve-your-python-understanding-pythons-execution-model/)
