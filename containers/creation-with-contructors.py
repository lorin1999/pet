aList = list((1, 2.0, 'hello', []))
aSet = set(([1, 2.0, 'hello']))
aTuple = tuple([1, 2.0, 'hello', []])
aString = str(['a', 'b', 'c'])
aDict = dict(key1='value', key2=1j, key3=[1, 2, {}])
iterables = [
    aList,
    aSet,
    aString,
    aDict,
]

for iterable in iterables:
    print iterable, (type(iterable))
