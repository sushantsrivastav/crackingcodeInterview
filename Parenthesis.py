#Implement an algorithm to print all valid (e.g., properly opened and closed) combinations of n pairs of parentheses.
# EXAMPLE
# Input: 3
#output = ['((()))', '(()())', '(())()', '()(())', '()()()']

def paren(n, partial="", open_count=0, close_count=0):
    if open_count + close_count == 2*n:
        return [partial]
    parens = []
    if open_count < n:
        parens += paren(n,partial + '(',open_count+1,close_count)
    if close_count < open_count:
        parens += paren(n,partial+')',open_count,close_count+1)
    return parens


print(paren(3))


