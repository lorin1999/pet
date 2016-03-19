# Introduction to Python Introspection

> Your visions will become clear only when you can look into your own heart. Who looks outside, dreams; who looks inside, awakes. 
    
> ― C.G. Jung

Most of the introspection introductions deal with the inbuilt capabilities of Python and how to use them in a REPL. I will instead concentrate here on a mix of using PyCharms capabilities and little scripts using the introspective capabilities of Python. I might stretch the classic definition of introspection a bit here, as I am understanding it as well as exploring your project, the standard library and third party libraries.

## The PyCharm way of introspection

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
import collections

collections.Hashable
```

## Further resources

Here is a good [old-school tutorial](http://www.ibm.com/developerworks/library/l-pyint/) to introspection if you want to explore that a bit more.

The [inspect module](https://docs.python.org/2/library/inspect.html) contains a lot of useful functions for more advanced programmatic introspection 
