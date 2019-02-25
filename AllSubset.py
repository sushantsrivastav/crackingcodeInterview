#Find all seubset of a set

import math
def allsubset(s):
    s = list(set(s))
    setsize = len(s)
    subsetsize = int(math.pow(2,setsize))

    j = 0
    rlist = []

    for counter in range(subsetsize):
        alist = []
        for j in range(setsize):
            if counter & ( 1 << j) > 0:
                alist.append(s[j])
        rlist.append(alist)
    return rlist

s = ['a','b','c','d','a']
print(allsubset(s))
