#Recursive Solution

def fib_rec(n):
    if n == 0 or n == 1 :
        return n
    return fib_rec(n-1) + fib_rec(n-2)

#using memoization
def fib_memo(n):
    memo = [0] * (n+1)
    return fib(n,memo)

def fib(i,memo):
    if i == 0 or i == 1:
        return i
    if memo[i] == 0:
        memo[i] = fib(i-1,memo) + fib(i-2,memo)
    return memo[i]

#bottom up DP

def fib_dp(n):
    if n == 0 or n == 1:
        return n
    a = 0
    b = 1
    for i in range(2,n):
        c = a+b
        a = b
        b = c
    return a+b
print(fib_rec(5))
print(fib_memo(5))
print (fib_dp(5))
