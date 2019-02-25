#Write a function to determine the number of bits you would need to flip to convert integer A to integer B.
# EXAMPLE Input: Output: 29 (or: 111131), 15 (or: 131111) 2


def conversion(a,b):
    c = a ^ b
    count = 0
    while c !=0:
        count += 1
        c = c & (c-1)
    return count

print(conversion(29,15))

