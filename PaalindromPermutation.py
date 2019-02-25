#Given a string, write a function to check if it is a permutation of a palindrome.
#  A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

def palindromCheck(s):
    char_set = set()
    for char in s:
        if char in char_set:
            char_set.remove(char)
        else :
            char_set.add(char)
    return len(char_set) <= 1

print(palindromCheck('abc'))
print(palindromCheck('aba'))
