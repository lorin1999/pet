# Containers! They are everywhere !1!!

![image](containers.jpg)

Containers and the intuitive way of working with them are one of the features of Python that can make you productive with the language right from the start. They are also an integral part of the internal language mechanics, so understanding them is essential tp understand how Python as a language ticks.

## What can I put in?

That depends on the container. Lists are the most welcoming containers, you can put in anything. Other containers (e.g. sets and tuples and dicts for their keys) need something hashable (we see that later in demo).

## Containers are iterable

All native container types 

## What makes a container out of an object? 

If the objects has a `__contains__` method it is a container and you can use the `in` operator to check if an object is in your container.

```python
myObject = 1
myContainer = [myObject]
if myObject in myContainer:
    print "WOHOO!"
```

OUT:

    WOHOO!
    
This works exactly the same for classes that you define and equip with a `__contains__` method

[demo](inspect-objects.py)

# Containers as part of the Python language mechanics

Every module contains dictionaries holding all the objects in the namespace of that module. Check out the `locals()` and `globals()` builtins

Everything in Python is an object and almost every object contains a dictionary holding attributes and methods
