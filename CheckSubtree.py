#Tl and T2 are two very large binary trees, with Tl much bigger than T2.
# Create an algorithm to determine if T2 is a subtree of Tl. A tree T2 is a subtree ofTi
# if there exists a node n in Ti such that the subtree of n is identical to T2.
# That is, if you cut off the tree at node n, the two trees would be identical.

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def isSubtree(s,t):
    return traverse(s,t)

def traverse(s,t):
    return s != None and (equals(s,t) or traverse(s.left,t) or traverse(s.right,t))

def equals(s,t):
    if s is None and t is None:
        return True
    if s is None or t is None:
        return False
    return s.val == t.val and equals(s.left,t.left) and equals(s.right,t.right)
