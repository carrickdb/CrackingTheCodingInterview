def next_number(n):
    z, o = 0,0
    mask = 1
    copy = n
    while mask & copy == 0:
        z += 1
        copy >>= 1
    while mask & copy == 1:
        o += 1
        copy >>= 1

    # Wipe out rightmost 1s and 0s
    mask = 1 << z+o
    mask -= 1
    mask = ~mask
    n &= mask

    # Add back 1 1
    mask = 1 << z+o
    n |= mask

    # Add back 1s all the way to the right
    mask = 1 << (o-1)
    mask -= 1
    n |= mask
    return n

def prev_number(n):
    z,o = 0,0
    mask = 1
    copy = n
    while copy & mask == 1:
        copy >>= 1
        o += 1
    if copy == 0: # all 1's
        return -1
    while copy & mask == 0:
        z += 1
        copy >>= 1

    # wipe out everything to right
    mask = ~((1 << (z+o+1)) - 1)
    n &= mask

    mask = ((1 << (o+1)) - 1) << (z - 1)
    n |= mask
    return n





for i in range(20,33):
    # print(i, next_number(i))
    print(str(i) + '\t' + str(prev_number(i)))
