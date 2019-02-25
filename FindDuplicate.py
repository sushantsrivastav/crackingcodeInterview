## You have an array with all the numbers from 1 to N, where N is at most 32,000. The array may have
# duplicate entries and you do not know what N is. With only 4 kilobytes of memory available, how
# would you print all duplicate elements in the array?

def findDuplicate(num):
    bit_vector = [0] * 500
    for n in num:
        vector_position = (n-1)//64
        vector_offset = (n-1)%64
        if bit_vector[vector_position] & (1 << vector_offset) == 0:
            bit_vector[vector_position] |= (1 << vector_offset)
        else:
            print(n)

a = []

for i in range(32000):
    a.append(i)
a[23322] = 22222
a[222] = 7777

findDuplicate(a)