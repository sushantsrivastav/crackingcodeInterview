#You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B.
# Write a method to merge B into A in sorted order.

def merge(num1,m,num2,n):
    while n > 0:
        if num2[n-1] > num1[m-1] or m <=0:
            num1[m+n-1] = num2[n-1]
            n -= 1
        else:
            num1[m+n-1] = num1[m-1]
            m -= 1
    return num1

A = [0]*6
A[0] = 1
A[1] = 4
A[2] = 6

B = [2,3,5]

print(merge(A,3,B,3))
