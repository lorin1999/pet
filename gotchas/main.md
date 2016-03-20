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


# More

[python gotchas](https://pythonconquerstheuniverse.wordpress.com/category/python-gotchas/)

[common mistakes](https://www.toptal.com/python/top-10-mistakes-that-python-programmers-make)
