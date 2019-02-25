#Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
# Implement a method to count how many possible ways the child can run up the stairs.

#recursive
def count_ways(n):
    if n < 0 :
        return  0
    elif n == 0 :
        return  1
    else:
        return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)

#Using memoizatuon

def count_ways_memo(n):
    memo = [-1] * (n+1)
    return count_ways_memo_helper(n,memo)

def count_ways_memo_helper(n,memo):
    if n < 0 :
        return 0
    elif n == 0:
        return 1
    elif memo[n] > -1:
        return memo[n]
    else:
        memo[n] = count_ways_memo_helper(n-1,memo) + count_ways_memo_helper(n-2,memo)+ count_ways_memo_helper(n-3,memo)
        return memo[n]