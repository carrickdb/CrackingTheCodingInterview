def replaceSpaces(st, trueLen):
    s = list(st)
    end = trueLen - 1
    numSpaces = st[:trueLen].count(' ')
    p = end + numSpaces*2
    while end >= 0:
        if s[end] != ' ':
            s[p] = s[end]
            p -= 1
        else:
            for ch in ['0', '2', '%']:
                s[p] = ch
                p -= 1
        end -= 1
    return ''.join(s)


s = "Mr John Smith        "
print(replaceSpaces(s, 13))
