

def test(foo, i):
    if i==5:
        return
    foo.add(i)
    print(foo)
    test(foo, i+1)


test(set(), 0)