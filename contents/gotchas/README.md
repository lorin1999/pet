# Accidentally creating a tuple

When editing away it is always possible that a rogue comma keeps sticking at the end of the line where it shouldn't be. Often it is a syntax error, but after an assignment it does not cause an error, but silently creates a tuple, when you actually wanted to create a list, like in the next example. Depending in the context and the quality of your logging and error handling this can be a tricky one to debug.

There is a good historical reason tor that though:

> One consequence of adding an array-like interface to tuples is that I had to figure out some way to resolve the edge cases of tuples with length 0 or 1. One of the rules I took from ABC was that every data type, when printed or converted to a string, should be represented by an expression that was a valid input to the language’s parser. So, it followed that I needed to have notations for 0- and 1-length tuples. At the same time I didn’t want to lose the distinction between a one-tuple and a bare parenthesized expression, so I settled for an ugly but pragmatic approach where a trailing comma would turn an expression into a one-tuple and "()" would represent a zero-tuple. It's worth nothing that parentheses aren’t normally required by Python’s tuple syntax, except here--I felt representing the empty tuple by “nothing” could too easily mask genuine typos.

> -- [Guido van Rossum - Early Language Design and Development](http://python-history.blogspot.de/2009/02/early-language-design-and-development.html)

```python
a = [1, 2, 3, 4, 5],
print type(a)
```

# Accidentally concatenating strings in a container

This can happen everywhere, where you pass in lists of string (or want to) but
actually you pass in one string, this can be quite tricky to find:

```python
l = [
    'some', 
    'list' 
    'of',
    'words'
]
```

'list' and 'of' are concatenated to one string 'listof' which is not what you wanted and will lead to surprises down the line.

# Mutable objects as default arguments 

`def fun(kw=[])` creates a function object and binds it to the current namespace (e.g. the module namespace if the definition is in a module).

The default arguments are evaluated exactly once as part of the function object creation. The objects defined as default arguments are also created and bound to the same namespace.

# Ambiguous meaning of the dot

```python
a = 1
a.bit_length()
```
OUT:

    1
    
```python
1.bit_length()
```
OUT:
   
    File "<input>", line 1
      1.bit_length
                 ^
    SyntaxError: invalid syntax

If you access the object attributes of an int directly, the meaning of the dot as the decimal dot is shadowing the attribute acces meaning if it, so it results in a syntax error.

The Language Parser of Python is very simple and just walks through the code from left to right and terminates the symbols without context.

## Solution

The int object has to be created first and then accessed. This is realized by explicitly reordering the execution by putting either a space between the int literal and the dot or wrap it in parentheses, which leads to a termination of the symbol and the creation of the object, which then can be accessed by the dot.

```python
1 .bit_length()
# <- note the space between the literal and the dot

(1).bit_length()
```

OUT:
   
    1
    1

```python
class A(object):
    a = 41
    # wird beim Erzeugen der Klasse ausgewertet
    b = [a + n for n in range(1, 3)]
    # a ist an globalen Namensraum gebunden
    c = (a + n for n in range(3, 5))
```

[DEMO](http://goo.gl/I6owCQ)

# (obsolete) Total ordering gotcha

[rich comparison the right way](https://regebro.wordpress.com/2010/12/13/python-implementing-rich-comparison-the-correct-way/)

Thanks to `functools.total_ordering` not a gotcha anymore ..._

# Generator vs list

[example](lists-vs-generators.py)

# circular imports

# Import traps

[import trapts](http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html)

# More


[python gotchas](https://pythonconquerstheuniverse.wordpress.com/category/python-gotchas/)

[common mistakes](https://www.toptal.com/python/top-10-mistakes-that-python-programmers-make)

