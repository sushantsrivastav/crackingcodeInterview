#Write a method to compute all permutations of a string of unique characters.


def permutations(s):
    return partial_permutation('',s)

def partial_permutation(partail,letter_left):
    if len(letter_left) == 0:
        return [partail]
    permutation = []

    for i, letter in enumerate(letter_left):
        next_letter_left = letter_left[:i] + letter_left[i+1:]
        permutation += partial_permutation(partail + letter, next_letter_left)
    return permutation

print(permutations('abc'))