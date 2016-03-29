import collections


def func():
    pass


class Cnt(object):
    """Container but not iterable"""
    def __contains__(self, _):
        return True


for obj in [1, 1l, 1.0, 1j, 's', None, True, [], (1, 2), {}, {1},
            object, collections, file('containers.py'), buffer('s'),
            func, Cnt, Cnt()]:
    isContainer = isinstance(obj, collections.Container)
    isIterable = isinstance(obj, collections.Iterable)
    isHashable = isinstance(obj, collections.Hashable)
    print ("%s: container: %s; sequence: %s; hashable: %s" %
           (type(obj), isContainer, isIterable, isHashable))
