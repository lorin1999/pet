# 1st Session 22 March 2016

## What we did

We made sure that everybody has ...
 
* A Python Interpreter (**[version 2.7](https://www.python.org/download/releases/2.7/)**) installed
* [PyCharm](https://www.jetbrains.com/pycharm/download/) installed.
* Created their [first PyCharm project](https://www.jetbrains.com/help/pycharm/5.0/creating-and-running-your-first-python-project.html)
* Created a new [virtualenv](https://www.jetbrains.com/help/pycharm/5.0/creating-virtual-environment.html) attached attached to that project
* Ran their first ["Hello, world" program](https://github.com/leachim6/hello-world/blob/master/p/python.py)

## What we learned (hopefully ;))

### Basic tools

* [Markdown](https://guides.github.com/features/mastering-markdown/) (extension .md) for writing formatted text that renders nicely e.g. on Github and can be converted into a lot of different formats.
* [Git](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control) for Version Control
* [Github](https://github.com/) for collaboration (and accessing these materials)
* [Pull Requests (PRs)](https://help.github.com/articles/using-pull-requests/) for proposing changes

### Spaces (and other special characters) in filenames are evil

[![spaces in filenames are evil](spaces-in-filenames-are-evil.jpg)](http://superuser.com/a/29117/381937)

### Quick overview about some central tools

See [Tools for exploration](../introspection/main.md#tools-for-exploration)

### Code block separation by indentation (significant whitespace)

Python is a language where space matters ... meaning  units of code (blocks, function bodies, etc.) are separated by ending a line with a colon (:) and [indenting](http://www.diveintopython.net/getting_to_know_python/indenting_code.html) (with the `Tab` key) the following code belonging to that block. The block is closed by [outdenting](https://www.jetbrains.com/help/pycharm/5.0/changing-indentation.html?) (with `Shift + Tab`) the first line that should not be part of that block anymore - a.k.a. [significant whitespace](https://www.python.org/dev/peps/pep-0008/#code-lay-out).

Example:

```python
def my_super_function():
    print "I am indented with 4 spaces"
    print "Me too! I belong to the function"
print "I am not inside the function block anymore :("

for currentElement in range(5):
    print currentElement
    print "I also belong to the loop block"
print "I don't belong to the loop block anymore"
```

Here are some articles that throw some light on the debate (yes ... there are people seriously arguing about the best way how to mark code blocks in programming languages).

* [Python: Myths about Indentation](http://www.secnetix.de/olli/Python/block_indentation.hawk)
* [What is Python Whitespace and how does it work?](http://stackoverflow.com/questions/13884499/what-is-python-whitespace-and-how-does-it-work)
* [Python White Space Discussion](http://c2.com/cgi/wiki?PythonWhiteSpaceDiscussion)
### Everything in Python is an object (even functions and classes)

In this [Python Online Tutor example](http://goo.gl/Yqt7hL) you can see how everything in a running Python program is an object. What you can do with those objects, we will explore next time.

### Easter eggs

Python has [insider jokes](../internals/easter-eggs.ipynb)!

## Where we go ...

It was suggested that we build a simple program directly in PyCharm that demonstrates the basic concepts we talked about. How about a simple object [introspection function](https://github.com/obestwalter/python-course/blob/master/introspection/introspection-function.ipynb)? I know I go on about this introspection and object stuff, but I really believe, that if you understand these concepts you are a long way in learning Python in a way that you actually understand what you're doing, when you write your first simple programs.