def isSubstring(a,b):
    return a in b


def isRotation(s1,s2):
    return len(s2) == len(s1) and isSubstring(s1, s2+s2)

print(isRotation("erbottlewat", "waterbottle"))

print(isRotation("foo", "waterbottle"))

print(isRotation("erbottlewate", "waterbottle"))

print(isRotation("", ""))