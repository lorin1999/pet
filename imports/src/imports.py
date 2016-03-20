import sys

import innerpackage
import mod1
import mod2

print mod1
print mod2.some_function
print mod2.someName

print sys.path

try:
    # the module inside the package is not imported automatically
    print innerpackage.innermod
except AttributeError as e:
    print e
    import innerpackage.innermod

    # now it is imported
    print innerpackage.innermod
