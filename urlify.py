#Write a method to replace all spaces in a string with '%20:
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string.
# (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)


def urlify(s,n):
    space_count = 0
    for char in s:
        if char == ' ':
            space_count += 1
    index = n + 2*space_count

    for i in range(len(s)-1,-1,-1):
        if s[i] == ' ':
            s[index-1] = '0'
            s[index-2] = '2'
            s[index-3] = '%'
            index = index-3
        else:
            s[index-1] = s[i]
            index -= 1
    return s