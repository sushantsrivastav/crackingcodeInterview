#Write a method to compute all permutations of a string whose characters are not necessarily unique.
# The list of permutations should not have duplicates.

def permutations(s):
    return partial_permutation('',sorted(s))

def partial_permutation(partial, letter_left):
    if len(letter_left) == 0:
        return [partial]
    permutation = []
    previous_letter = None
    for i,letter in enumerate(letter_left):
        if letter == previous_letter:
            continue
        next_letter_left = letter_left[:i] + letter_left[i+1:]
        permutation += partial_permutation(partial+letter,next_letter_left)
        previous_letter = letter
    return permutation


print(permutations('aba'))


