#Implement a function to check if a binary tree is balanced.
# For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the
# two subtrees of any node never differ by more than one.


class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def isBalanced(root):
    if root is None:
        return True
    def height(node,depth):
        if node is None:
            return None
        h1 = height(node.left,depth+1)
        h2 = height(node.right,depth+1)
        if h1 is None or h2 is None :
            return None
        return max(h1,h2) if abs(h1-h2) <= 1 else None
    ans = height(root,0)
    return True if ans else False