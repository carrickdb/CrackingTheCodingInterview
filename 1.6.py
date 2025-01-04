def compress(s):
    i = 0
    newstr = []
    curr  = None
    while i < len(s):
        j = i+1
        while j < len(s) and s[j] == s[i]:
            j += 1
        newstr.append(s[i])
        newstr.append(str(j-i))
        i = j

    newstr = ''.join(newstr)
    if len(newstr) >= len(s):
        return s
    return newstr

print(compress(""))
