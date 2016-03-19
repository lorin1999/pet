aString = "123456"
aList = [1, 2.0, 1j, 'hello', [], {}, (1, 2)]
aSet = {1, 2.0, 1j, 'hello', (1, 2)}
aTuple = (1, 2.0, 1j, 'hello', [], {}, (1, 2))
aDict = {
    1: 1,
    2.0: 2.0,
    1j: 1j,
    (1, 2): (1, 2),
    'hello': 'hello',
    'list': [],
    'dict': {},
}

iterables = [
    aString,
    aList,
    aSet,
    aTuple,
    aDict,
]


for iterable in iterables:
    print('iterating over %s' % (type(iterable)))
    for element in iterable:
        print element,
        if isinstance(iterable, dict):
            print '(value: %s)' % (str(iterable[element])),
    print
