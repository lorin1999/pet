"""This is the docstring of this module"""


def some_func():
    funcLocal = 1
    otherFuncLocal = "hello"
    show_callers_locals()
    print funcLocal, otherFuncLocal


def show_globals():
    print 'showing objects in global namespace'
    for k, v in sorted(globals().items()):
        print "%s: %s %s (%s)" % (k, v, type(v), id(v))
    print "#" * 100


def show_callers_locals():
    import inspect

    print 'showing objects in callers namespace'
    frame = inspect.currentframe()
    try:
        for k, v in sorted(frame.f_back.f_locals.items()):
            print "%s: %s %s (%s)" % (k, v, type(v), id(v))
        print "#" * 100
    finally:
        del frame

myVar = 1


class Klass(object):
    pass

klassInstance = Klass()

show_callers_locals()
show_globals()
some_func()
