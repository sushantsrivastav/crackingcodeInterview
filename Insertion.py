#You are given two 32-bit numbers, N and M, and two bit positions, i and j.
# Write a method to insert Minto N such that M starts at bit j and ends at bit i.
# You can assume that the bits j through i have enough space to fit all of M.
# That is, if M = 10011, you can assume that there are at least 5 bits between j and i.
# You would not, for example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.
# EXAMPLE
# Input: N = 10000000000, M= 10011, i 2, j 6
# Output: N 10001001100


def insertbit(M,N,i,j):
    allOne = ~0
    print(bin(allOne))
    left = allOne << (j+1)
    right = (1 << i) -1
    mask = left | right
    n_cleared = N & mask
    m_shifted = M << i
    return n_cleared | m_shifted

print(bin(insertbit(0b11111111,0b10,2,5)))
