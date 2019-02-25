#Write a method to sort an array of strings so that all the anagrams are next to each other.

def group_anagrams(a):
    anagram_map = {}

    for s in a:
        anagram = ''.join(sorted(s))
        if anagram in anagram_map:
            anagram_map[anagram].append(s)
        else:
            anagram_map[anagram] = [s]
    result = []

    for v in anagram_map.values():
        result += v
    return result


if __name__ == "__main__":
    a = ['aaa', 'bbb', 'ccc', 'abc', 'bca', 'cba']
    print(group_anagrams(a))