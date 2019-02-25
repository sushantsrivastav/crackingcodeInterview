#There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.
# EXAMPLE
# pale, pIe -> true
# pales. pale -> true
#  pale. bale -> true
# pale. bake -> false


def oneAway(s,t):
    l1 = len(s)
    l2 = len(t)
    if abs(l1-l2) > 1:
        return False
    if l1 <= l2:
        s1 = s
        s2 = t
    else:
        s1 = t
        s2 = s
    index1 = 0
    index2 = 0
    foundDiff = False

    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            if foundDiff :
                return False

            foundDiff = True
            if len(s1) == len(s2):
                index1 += 1
        else:
            index1 += 1
        index2 +=1
    return True



print(oneAway('pale','ple'))
print(oneAway('pales','pale'))
print(oneAway('pale','bale'))
print(oneAway('pale','bake'))


