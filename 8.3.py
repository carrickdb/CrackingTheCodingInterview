def get_magic_index(nums):
    s,e = 0,len(nums)
    while s<e:
        m = (s+e)//2
        if nums[m] == m:
            return m
        if nums[m] < m:
            s = m+1
        else:
            e = m
    return -1


print(get_magic_index([-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]))