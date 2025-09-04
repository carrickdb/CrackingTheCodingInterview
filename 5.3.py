from collections import deque

def longest_sequence(n):
    if n == 0:
        return 1
    mask = 1
    counts = deque([None, None, None])
    m = 0
    while mask <= n:
        count = 0
        while mask <= n and mask & n == 0:
            count += 1
            mask <<= 1
        if count > 0:
            counts.append((0, count))
            counts.popleft()
        count = 0
        while mask <= n and mask & n != 0:
            count += 1
            mask <<= 1
        if count > 0:
            counts.append((1, count))
            counts.popleft()
        if counts[0] == None:
            continue
        if counts[1][0] == 0:
            o1, z, o2 = counts[0][1], counts[1][1], counts[2][1]
            if z == 1:
                m = max(m, o1+1+o2)
            else:
                m = max(m, o1+1)
    m = max(m, counts[-1][1] + 1)
    return m


for i in [1775, 0b101100110, 0b1000011001001, 0, 0b1011011, 0b110, 0b1]:
    print(i, end=' ')
    print(longest_sequence(i))


# def longest_sequence(n):
#     if n == 0:
#         return 1
#     mask = 1
#     counts = []
#     m = 0
#     while mask <= n:
#         count = 0
#         while mask <= n and mask & n == 0:
#             count += 1
#             mask <<= 1
#         if count > 0:
#             counts.append((0, count))
#         count = 0
#         while mask <= n and mask & n != 0:
#             count += 1
#             mask <<= 1
#         if count > 0:
#             counts.append((1, count))
#     l = len(counts)
#     for i in range(1, l-1):
#         if counts[i][0] == 0:
#             o1,z,o2 = counts[i-1][1], counts[i][1], counts[i+1][1]
#             if z == 1:
#                 m = max(m, o1+1+o2)
#             else:
#                 m = max(m, o1+1)
#     m = max(m, counts[-1][1] + 1)
#     return m
