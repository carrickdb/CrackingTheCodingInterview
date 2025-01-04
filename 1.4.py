def couldBePalindrome(s):
    charCounts = {}
    for c in s:
        if c not in charCounts:
            charCounts[c] = 0
        charCounts[c] += 1
    numOdd = sum([x%2 for x in charCounts.values()])
    return numOdd < 2

print(couldBePalindrome('baa'))
