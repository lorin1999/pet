
def print_introspection_info(obj):
    print "inspect all public attributes of %s id(%s)" % (type(obj), id(obj))
    for name in dir(obj):
        if name.startswith('_'):
            continue

        value = getattr(obj, name)
        valueType = type(value)
        print "## %s | %s | %s ##" % (name, value, valueType)
        help(value)  # a bit fancier than just print value.__doc__
        print "-" * 120


objs = [1, 1.0, 's', [], {}, tuple(), set()]
assert isinstance(objs, list)
for obj in objs:
    print_introspection_info(obj)
    print "#" * 120
