import collections


def func():
    pass


class Cnt(object):
    def __contains__(self, _):
        return True


for obj in [1, 1l, 1.0, 1j, 's', None, True, [], (1, 2), {}, {1},
            object, collections, file('containers.py'), buffer('s'),
            func, Cnt, Cnt()]:
    msg = '' if isinstance(obj, collections.Container) else 'NOT '
    print "%s is %sa container" % (type(obj), msg)
