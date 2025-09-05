def draw_line(screen, w, x1, x2, y):
    if x2 <= (x1//8*8) + 7:
        num_ones = x2 - x1 + 1
        m = ((1<<(num_ones)) - 1) << 7 - x2
        screen[w*y + x1//8] |= m
        return
    first_full = x1//8
    if x1%8 != 0:
        m = (1 << (8 - x1%8)) - 1
        screen[w*y+first_full] |= m
        first_full += 1
    last_full = x2//8
    if x2%8 != 7:
        num_ones = (x2%8) + 1
        m = ((1 << num_ones) - 1) << (8 - num_ones)
        screen[w*y+last_full] |= m
        last_full -= 1
    for i in range(first_full, last_full+1):
        screen[w*y+i] = 0xFF

def print_screen(screen, w):
    for i in range(len(screen)//w):
        for j in range(w):
            m = 1 << 7
            for k in range(8):
                if m & screen[i*w + j] != 0:
                    print("-", end="")
                else:
                    print(".", end="")
                m >>= 1
        print()


w = 7
screen = bytearray([0x00] * 7*11)
draw_line(screen, w, 11,55, 4)

print_screen(screen, w)