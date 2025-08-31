
def insertInt(n,m, i,j):
    mask = (1<<(n.bit_length() - j+1)) - 1
    # print(bin(mask))
    mask <<= (j + 1)
    # print(bin(mask))
    secondMask = (1<<i) - 1
    # print(bin(secondMask))
    mask |= secondMask
    print(bin(mask))
    n &= mask
    # print(bin(n))
    m <<= i
    # print(bin(m))
    return n | m



n = 0b10000000000000
m = 0b10011

n = 0b101011101101
m =  0b1000001
i = 4

# n = 0b10101
# m = 0b101
# i = 1
j = i+m.bit_length()-1
print(bin(insertInt(n,m,i,j)))
