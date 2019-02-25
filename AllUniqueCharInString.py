#Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

#Approach1 using set
# time complexity and space complexity to liner O(n)
def uniqueCharacter1(s):
    char_set = set()

    for char in s :
        if char in char_set:
            return False
        else:
            char_set.add(char)
    return True

#Approach 2
# minimizing the space complexity to constant

def uniqueCharacter2(s):
    char_freq = [0] * 26
    for char in s:
        index = ord(char) - ord('a')
        char_freq[index] += 1

        if char_freq[index] > 1 :
            return False
    return True

#Approach 3
# Additional Data Structure is not involved
#using bit manipulation

def uniqueCharacter3(s):
    checker = 0
    for char in s:
        bitIndex = ord(char) - ord('a')
        if checker & (1 << bitIndex) > 0 :
            return False
        checker = checker | (1 << bitIndex)
    return True


print("###using first approach###")
print(uniqueCharacter1('abcde'))
print(uniqueCharacter1('abcda'))
print("###using second approach###")
print(uniqueCharacter2('abcde'))
print(uniqueCharacter2('abcda'))
print("###using Third approach###")
print(uniqueCharacter3('abcde'))
print(uniqueCharacter3('abcda'))
