# Introspection exercises

### Basics

* print the path of the Python Interpreter you script or REPL is using.

* print the type of `42` (the int

* print all attributes and functions of `42`

* print the type of the `sys` module

* print the path to the file that contains the `sys` module

#### lists
 
Use this list as starting point:

```python
l = [1, 4, 4, 1, 7, 2, 4, 2, 1, 0]
```

* create a sequence based on `l` that has no duplicates

* create an **ordered** sequence based on `l` that has no duplicates

* create a sequence based on `l` that has no duplicates preserving the original order of `l`

* remove the first element of the list

#### paths

* print the full paths of all directories in the root of your PyCharm project folder

* print the full paths of all directories in your PyCharm project folder independently from where you started the script (e.g. if your script is in /home/scripts/myscript, it should also work if you start the script from /home)

* print only the names of all files in your PyCharm project folder

* print a sorted ist of the names of all files in your PyCharm project folder

* print only the names of all xml files in your PyCharm project

#### `globals()` and `locals()`

open an empty module and type:

myVar = 1

Now change the value to 'hello' but you are not allowed to set it directly with `myVar = "hello"`
