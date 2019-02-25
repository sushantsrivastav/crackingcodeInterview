#Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.


def checkPermutation(s,t):
    char_freq = [0] * 128

    if len(s) != len(t):
        return False
    for char in s:
        index = ord(char) - ord('a')
        char_freq[index] += 1

    for char in t:
        index = ord(char) - ord('a')
        char_freq[index] -= 1
        if char_freq[index] < 0 :
            return False
    return True

print(checkPermutation('dog','god'))
print(checkPermutation('abcd','abc'))
print(checkPermutation('abc','abe'))

