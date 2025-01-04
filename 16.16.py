def findMinSort(arr):
    if len(arr) < 2:
        return 0
    start = 0
    while start < len(arr)-1:
        if arr[start] > arr[start+1]:
            break
        start += 1
    if start >= len(arr)-1:
        return 0
    end = len(arr)-1
    while end >= 0:
        if arr[end] < arr[end-1]:
            break
        end -= 1
    maxNum = max(arr[start:end+1])
    minNum = min(arr[start:end+1])
    m, n = 0, 0
    for i in range(len(arr)):
        if arr[i] > minNum:
            m = i
            break
    for j in range(len(arr)-1, -1, -1):
        if arr[j] < maxNum:
            n = j
            break
    return (m,n)


arr = [5,2,7]
print(findMinSort(arr))
