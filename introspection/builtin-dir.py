"""
Get help about an object

in default REPL:

    help(sys)

on command line:

    pydoc sys

in Ipython:

    sys?
"""


def print_object_attributes(obj):
    print "inspect all public attributes of %s" % type(obj)
    for name in dir(obj):
        if name.startswith('_'):
            continue

        value = getattr(obj, name)
        valueType = type(value)
        print "%s | %s | %s" % (name, value, valueType)
        help(value)  # a bit fancier than just print value.__doc__
        print "-" * 120


objs = [1, 1.0, 's', [], {}, tuple(), set()]
for obj in objs:
    print_object_attributes(obj)
    print "#" * 120
