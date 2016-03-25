# Internals

http://stackoverflow.com/questions/21233229/whats-the-purpose-of-the-package-attribute-in-python

https://docs.python.org/2.7/reference/toplevel_components.html#programs

https://docs.python.org/2.7/library/__builtin__.html#module-__builtin__

http://stackoverflow.com/questions/6618795/get-locals-from-calling-namespace-in-python

http://stackoverflow.com/questions/15077627/python-locals-for-containing-scope


# Advanced Introspection

If you start to get really curious to find out more about the guts of a Python script in execution you might encounter a few surprises.

If everything is just an object and namespaces are just dictionaries bound to e.g. modules containing all objects in scope ... where are they? (locals(), globals())

runtime error iterating over locals / (globals?)

deepcopy error

Why are functions that are always accessible not in locals (open(), etc) -> `__builtins__`

# Bonus Track

[easter eggs](easter-eggs.ipynb)
