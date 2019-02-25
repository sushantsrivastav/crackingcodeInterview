#Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree.
# Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


def firstCommAnsestor(root,p,q):
    if root is None:
        return None
    if root == p or root == q:
        return root
    left = firstCommAnsestor(root.left,p,q)
    right = firstCommAnsestor(root.right,p,q)

    if left and right :
        return root
    else :
        if left :
            return left
        else:
            return right
