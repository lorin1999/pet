# def is a an statement that creates a function object

`def fun(kw=[])` creates a function object and binds it to the current namespace (e.g. the module namespace if the definition is in a module).

the default arguments are evaluated exactly once as part of that object creation. The objects defined in default args are also created and bound to the same namespace.

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

The int object has to be created first and then accessed. This is realized by putting a space between the int literal and the dot, which leads to a termination of the symbol and the creation of the object, which then can be accessed by the dot.

```python
1 .bit_length()
# <- note the space between the literal and the dot
```

OUT:
   
    1
