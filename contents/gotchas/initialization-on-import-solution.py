def f(e, p=None):
    p = p or []
    p.append(e)
    return p

lists = []
for idx in range(5):
    lists.append(f(idx))
    print lists
print set(id(l) for l in lists)
