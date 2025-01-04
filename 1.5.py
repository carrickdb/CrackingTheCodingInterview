def oneEditAway(s1, s2):
    if abs(len(s1)-len(s2)) > 1:
        return False
    for i in range(len(min(s1, s2))):
        c1 = s1[i]
        c2 = s2[i]
        if c1!=c2:
            if len(s1) > len(s2):
                return s1[i+1:] == s2[i:]
            elif len(s1) < len(s2):
                return s1[i:] == s2[i+1:]
            else:
                return s1[i+1:] == s2[i+1:]
    return True


print(oneEditAway("pale", "ple"))
print(oneEditAway("pales", "pale"))
print(oneEditAway("pale", "bale"))
print(oneEditAway("pale", "bake"))
print(oneEditAway("ple", "pale"))
