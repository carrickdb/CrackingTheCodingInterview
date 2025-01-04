def hasAllUniqueCharacters(s):
    bitVector = [0 for i in range(16)]
    for char in s:
        i = ord(char)
        mask = 1 << (i%8)
        if bitVector[i//8] & mask:
            return False
        bitVector[i//8] |= mask
    return True



s = "apple"
print(hasAllUniqueCharacters(s))
