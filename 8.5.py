def mult_rec(a,b):
    if b == 1:
        return a
    if b == 0:
        return 0
    total = mult_rec(a, b>>1) << 1
    mask = 1
    if mask & b == 1:
        total += a
    return total


print(mult_rec(1,0))
print(mult_rec(5,4))
print(mult_rec(2,14))
print(mult_rec(5334,6566))
print(5334*6566)