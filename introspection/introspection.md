# Introduction to Python Introspection

> Your visions will become clear only when you can look into your own heart. Who looks outside, dreams; who looks inside, awakes. 
    
> ― C.G. Jung

## Classic introspection

* `id` returns an int that is the unique id for that object in memory
* `dir` takes an object and returns a list of all attribute names. With those you can explore the object further.
* `help` takes an object and prints the documentation for that object.
* `type` takes an object and returns a string representation of its type.
* `isinstance` tells you if the object is an instance of a given type
* the [inspect module](https://docs.python.org/2/library/inspect.html) contains a lot of useful functions for even more advanced introspection of live objects
* the [sys module](https://docs.python.org/2/library/sys.html#module-sys) contains information about the Python interpreter itself and the system the interpreter is running on. `sys.argv` is a list of command line arguments passed to the running script.
* the [sysconfig](https://docs.python.org/2/library/sysconfig.html#module-sysconfig) provides access to Python's configuration information like the list of installation paths and the configuration variables relevant for the current platform.

Here is a good [old-school tutorial](http://www.ibm.com/developerworks/library/l-pyint/) to introspection if you want to explore that a bit more.

### Demos

* [basic introspection demo](introspection.py)

## The PyCharm way of introspection

With classic ways of introspection of introductions out of the we can now look at here using PyCharms for introspection and code exploration. The capabilities for code exploration and introspection are built on top of the languages capabilities for introspection offering a convenient interface to them.

## Reading documentation and source code

PyCharm offers a lot of actions to provide information about elements of your project. The most useful here are:

* Quick Documentation
* Quick Definition
* Go to Declaration

Invoking any of those actions with the cursor over a piece of code will provide more insight about that object.

You can query this information directly from the search popups to inspect the objects. As an example: If you want to know what you project contains to do with files you just type "file" in the "Search Everywhere" popup and get offered the file builtin, you can scroll down to that entry and invoke the Quick Documentation action and you see the documentation including a link to the external documentation on the web.

## Auto Completion

Code completion is actually also a form of introspection that helps you figuring out what you can do with the objects in your code. Pycharm has basic and SmartType completion.I don't quite get the smart in smartType it just offers you lots of types. Autocompletion is [quite versatile](https://www.jetbrains.com/help/pycharm/5.0/auto-completing-code.html?origin=old_help).

You can even use completion and query features in this markdown document:

```python
import inspect

inspect.getcallargs(inspect.getargs)
```
