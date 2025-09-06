def swap(a,b):
    a ^= b
    b ^= a
    a ^= b
    return a,b


a = 5
b = 2
print(swap(a,b))
