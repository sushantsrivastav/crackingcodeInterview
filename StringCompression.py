#Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2b1c5a3.
# If the "compressed" string would not become smaller than the original string,
#  your method should return the original string.
# You can assume the string has only uppercase and lowercase letters (a - z).

def stringCompress(chars):
    anchor = 0
    ans = ''
    for read, char in enumerate(chars):
        if read + 1 == len(chars) or char != chars[read+1]:
            ans += char
            if read >= anchor:
                for digit in str(read-anchor + 1):
                    ans += digit
            anchor = read +1
    return ans

print(stringCompress('aabcccccaaa'))


