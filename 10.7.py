from random import randint
import struct, math

filename = "numbers.dat"

def generate_file():
    a = set()
    for i in range(700):
        a.add(i)
    for i in range(1300):
        while True:
            r = randint(700,2**15-1)
            if r not in a:
                a.add(r)
                print(r)
                break
    with open(filename, 'wb') as f:
        for num in a:
            f.write(struct.pack('<h', num))

generate_file()

n = int(math.ceil(pow(2, 7.5)))

def get_nums():
    with open(filename, 'rb') as f:
        while True:
            bytes_read = f.read(2)
            if not bytes_read:
                break
            num = struct.unpack('<h', bytes_read)[0]
            yield num

def check_blocks():
    arr = [0 for _ in range(n)]
    for num in get_nums():
        try:
            arr[num//n] += 1
        except:
            print("num//n", num, n, num//n)
    return arr

arr = check_blocks()

def get_missing_int(a):
    for i, count in enumerate(a):
        bitmap = 0
        if count < n:
            for num in get_nums():
                num -= n*i
                if 0 <= num <= n:
                    mask = 1 << num
                    bitmap |= mask
            mask = 1
            count = 0
            while bitmap > 0:
                if bitmap & mask != 1:
                    return n*i + count
                count += 1
                bitmap >>= 1

missing_int = get_missing_int(arr)
print(missing_int)
for num in get_nums():
    if num==missing_int:
        print("oh no!", num)
print("yay")
