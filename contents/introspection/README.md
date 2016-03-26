# Introduction to Introspection

> Your visions will become clear only when you can look into your own heart. Who looks outside, dreams; who looks inside, awakes. 
    
> ― C.G. Jung

## Tools for exploration

### PythonTutor: Visualize code execution

[PythonTutor](http://www.pythontutor.com/visualize.html) is a great tool to see exactly what happens in memory when Python code is executed. You can step through each line and see the state of the execution frames and the object. This will give you a good foundation on which you can reason about the code you are developing, because you really know what is going on, instead of just guessing.

Try this [little introduction](http://goo.gl/CqhmVy)

### Ipython: Python interpreter on Steroids

The Python interpreter has an [interactive mode](https://docs.python.org/2/tutorial/interpreter.html#interactive-mode) (more generally known as Read Eval Print Loop - [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)). This provides a way of interactively developing and exploring program code. [Ipython](https://ipython.org/) enhances the interactive shell in many ways that provide more assistance to the explorer. Some central improvements are shell-like tab completion, shell commands, file completion, pretty tracebacks, magic commands (try `%quickref`) and easier introspection of live objects [(see main features)](http://ipython.readthedocs.org/en/stable/overview.html#main-features-of-the-interactive-shell). Getting help is much easier as well: instead of `help(sys)` you can type `sys?` to see the documentation and `sys??` to see the source code.

[Try Ipython online](https://www.pythonanywhere.com/try-ipython/).

### Jupyter: Interactive Notebooks

Jupyter notebooks - formerly known as Ipython notebooks - are a way to create documents that consist of code that can be executed directly from the document to fetch it's output. You can also use Markdown to create rich documents. The results can be saved and rendered in many different output formats. Github renders these Notebooks by default.

* [Official Documentation](https://jupyter.readthedocs.org/en/latest/#user-docs)
* [Alternative Manual](http://jupyter.cs.brynmawr.edu/hub/dblank/public/Jupyter%20Notebook%20Users%20Manual.ipynb#Jupyter-Notebook-Users-Manual)

Use Jupyter without installing it:

* [Try Jupyter online](https://try.jupyter.org/)
* [Wakari Notebook Hosting](https://wakari.io)

### Exploration and Introspection with a good IDE

[PyCharm](https://www.jetbrains.com/pycharm/) is my IDE of choice so everything in this course referring to using an IDE will be about that, although I am sure that [other IDEs](https://wiki.python.org/moin/IntegratedDevelopmentEnvironments) offer similar features.

An IDE that indexes and analyzes the Code in your project and all installed libraries is a very powerful tool to explore the language itself and learn a lot by reading source code and documentation directly where you are working with it. Powerful [debugging support](https://www.youtube.com/watch?v=JcOCNgXXhmE&list=PLQ176FUIyIUY5Ii58pzoZhS_3qIBL80nz) also goes a long way in helping you ti understand you own or other peoples code and catch your wrong assumptions about what is supposedly going on. The capabilities for code exploration and introspection in PyCharm are built on top of the languages capabilities for introspection offering a convenient interface to them.

#### Reading documentation and source code

PyCharm offers a lot of actions to provide information about elements of your project. The most useful here are:

* [Quick Documentation](https://www.jetbrains.com/help/pycharm/5.0/viewing-inline-documentation.html)
* [Quick Definition](https://www.jetbrains.com/help/pycharm/5.0/viewing-definition.html)
* [Go to Declaration](https://www.jetbrains.com/help/pycharm/5.0/navigating-to-declaration-or-type-declaration-of-a-symbol.html)

Invoking any of those actions with the cursor over a piece of code will provide more insight about that object.

You can query this information directly from the search popups to inspect the objects. As an example: If you want to know what you project contains to do with files you just type "file" in the "Search Everywhere" popup and get offered the file builtin, you can scroll down to that entry and invoke the Quick Documentation action and you see the documentation including a link to the external documentation on the web.

#### Structure Tool Window

The [Structure Tool Window](https://www.jetbrains.com/help/idea/2016.1/structure-tool-window-file-structure-popup.html) makes all classes and functions explorable from a bird's eye perspective.

### Code Navigation

There are a [lot of ways to navigate in the code](https://www.jetbrains.com/help/pycharm/5.0/navigation-in-source-code.html) which is what you do a lot, when you work with larger code bases an/or work with a lot of libraries. The best documentation is often the source code and if it's easy to have a quick look at a module you are using this often is all you need in way of documentation.

You can navigate the code by activating the ["Goto Declaration"](https://www.jetbrains.com/help/pycharm/5.0/navigating-to-declaration-or-type-declaration-of-a-symbol.html) Action or by holding down `Ctrl` and clicking with the mouse on the object to go to the source code of the referenced object. The "Navigate Back" action (`Alt+left`) brings you back to the old position just like the history function in a web browser. This way of navigating through the code lets you see the code as a collection of connected objects instead of as just text.

* [All resources about navigation in PyCharm](https://www.jetbrains.com/help/pycharm/5.0/navigating-to-declaration-or-type-declaration-of-a-symbol.html)

### Auto Completion

This (especially in combination with "Quick Documentation" and "Quick Definition" directly from the completion popup) is actually also a very effective way to explore the code. Pycharm has basic and SmartType completion. I don't quite get the smart in smartType though ... it just offers you lots of types which are currently not imported. Auto Completion is [quite versatile](https://www.jetbrains.com/help/pycharm/5.0/auto-completing-code.html?origin=old_help).


#### PyCharm Auto completion works even in Markdown

You can even use completion and query features in this markdown document **(this only works if you have this file open in PyCharm)**:

```python
import inspect

inspect.getcallargs(inspect.getargs)
```

## Classic introspection in Python

* [`help`](https://docs.python.org/2/library/functions.html#help) takes an object and prints the documentation for that object.
* [`dir`](https://docs.python.org/2/library/functions.html#dir) takes an object and returns a list of all attribute names. With those you can explore the object further.
* [`type`](https://docs.python.org/2/library/functions.html#type) takes an object and returns a string representation of its type.
* [`isinstance`](https://docs.python.org/2/library/functions.html#isinstance) tells you if the object is an instance of a given type.
* the [inspect module](https://docs.python.org/2/library/inspect.html) contains a lot of useful functions for even more advanced introspection of live objects. See also this [great article](https://pymotw.com/2/inspect/index.html#module-inspect).
* the [sys module](https://docs.python.org/2/library/sys.html#module-sys) contains information about the Python interpreter itself and the system the interpreter is running on. [`sys.argv`](https://docs.python.org/2/library/sys.html#sys.argv) is a list of command line arguments passed to the running script.
* the [sysconfig](https://docs.python.org/2/library/sysconfig.html#module-sysconfig) module provides access to Python's configuration information like the list of installation paths and the configuration variables relevant for the current platform.
* [`id`](https://docs.python.org/2/library/functions.html#id) returns an int that is the unique id for that object in memory.

Here is a good [old-school tutorial](http://www.ibm.com/developerworks/library/l-pyint/) to introspection if you want to explore that a bit more.

### Ipython introspection demos

The following examples demonstrate some more introspection activities with the help of Jupyter notebooks: 
 
* [Basic Introspection](introspection-basics.ipynb) 
* [Accessing system information](introspection-system.ipynb) 
* [A simple introspection function](introspection-function.ipynb).

If you clone this repository and install Jupyter you can open these Notebooks and experiment with them.
