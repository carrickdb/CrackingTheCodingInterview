def get_powerset(s, start):
    if start == len(s):
        return [[]]
    psets = get_powerset(s, start+1)
    l = len(psets)
    new_psets = []
    for pset in psets:
        new_psets.append(pset[:])
    for pset in psets:
        new_set = pset[:]
        new_set.append(s[start])
        new_psets.append(new_set)
    return new_psets

s = [1,2,3]
print(get_powerset(s, 0))