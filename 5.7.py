def swap_bits(n):
    return ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)


print(swap_bits(0b10011010111)==0b100011101011)

"""
 100011101011
0b10011010111

"""