#Write a recursive function to multiply two positive integers without using the * operator.
#  You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations.


def product(a,b):
    if a < 0 and b < 0 :
        sign = '+'
    elif a <0 or b < 0:
        sign = '-'
    else:
        sign = '+'
    a= abs(a)
    b = abs(b)
    if a < b:
        smaller = a
        bigger = b
    else:
        smaller = b
        bigger = a

    return int(sign + str(product_helper(smaller,bigger)))

def product_helper(smaller,bigger):
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger
    s = smaller >> 1
    half = product_helper(s,bigger)
    if (smaller %2 == 0):
        return half + half
    else :
        return half + half + bigger


print(product(-5,-7))