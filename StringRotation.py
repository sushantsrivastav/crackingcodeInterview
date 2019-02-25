#Assume you have a method isSubst ring which checks if one word is a substring of another.
# Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one call to isSubstring
# (e.g., "waterbottle" is a rotation of"erbottlewat").

def isRotatation(s1,s2):
    if len(s1) != len(s2):
        return False
    return s1 in(s2 + s2)


print(isRotatation('waterbottle','erbottlewat'))