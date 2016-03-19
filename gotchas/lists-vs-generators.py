class A(object):
    a = 41
    b = [a + n for n in range(1, 3)]
    c = (A.a + n for n in range(3, 5))
    d = (a + n for n in range(5, 7))

for e in A.b:
    print e

for e in A.c:
    print e

try:
    for e in A.d:
        print e
except NameError as e:
    print e
