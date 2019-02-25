#Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree.
# You may assume that each node has a link to its parent.

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def inOrderSuccesor(root,node):
    if node.right:
        curr = node.right
        while curr.left:
            curr = curr.left
        print(curr.val)
    else:
        curr = root
        suc = None
        while node.val != curr.val:
            if node.val < curr.val:
                suc = curr
                curr = curr.left
            else:
                curr = curr.right

        if suc :
            print suc.val
        else:
            print None




a = TreeNode(9)
b = TreeNode(5)
c = TreeNode(12)
d = TreeNode(1)
e = TreeNode(6)
f = TreeNode(10)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
root = a


inOrderSuccesor(a,f)

