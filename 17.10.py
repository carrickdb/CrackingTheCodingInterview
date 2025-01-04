def majorityElement(arr):
    majElement = -1
    count = 0
    for i in range(len(arr)):
        if majElement == -1:
            majElement = arr[i]
        if arr[i] == majElement:
            count += 1
        else:
            count -= 1
        if not count:
            majElement = -1
    if majElement != -1:
        if arr.count(majElement) <= len(arr)//2:
            majElement = -1
    return majElement


arr = [2,2,1,2,1,2,2,2,2,3,3,3,3,2,4]
print(len(arr))
print(arr.count(2))
"""
len(arr):
2: 7
"""
print(majorityElement(arr))
