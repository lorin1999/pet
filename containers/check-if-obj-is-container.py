import collections


def func():
    pass


class Cnt(object):
    """Container but no sequence"""
    def __contains__(self, _):
        return True


for obj in [1, 1l, 1.0, 1j, 's', None, True, [], (1, 2), {}, {1},
            object, collections, file('containers.py'), buffer('s'),
            func, Cnt, Cnt()]:
    isCnt = isinstance(obj, collections.Container)
    isIter = isinstance(obj, collections.Iterable)
    print "%s: container: %s; sequence: %s" % (type(obj), isCnt, isIter)
