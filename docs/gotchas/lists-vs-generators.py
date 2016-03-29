class A(object):
    a = 41
    b = [a + n for n in range(1, 3)]
    c = (A.a + n for n in range(3, 5))
    d = (a + n for n in range(5, 7))

for elem in A.b:
    print elem

for elem in A.c:
    print elem

try:
    for elem in A.d:
        print elem
except NameError as e:
    print e
