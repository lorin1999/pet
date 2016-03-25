def f(e, p=[]):
    p.append(e)
    return p

lists = []
for idx in range(5):
    lists.append(f(idx))
    print lists
print set(id(l) for l in lists)
