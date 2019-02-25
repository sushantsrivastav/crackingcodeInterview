class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


def validateBST(root):
    if root is None:
        return True
    node_and_bound_stack = [(root,float('-inf'),float('inf'))]

    while node_and_bound_stack:
        node, lower_bound, upper_bound = node_and_bound_stack.pop()
        if not lower_bound <= node.val < upper_bound:
            return False
        if node.left :
            node_and_bound_stack.append((node.left,float('-inf'),node.val))
        if node.right:
            node_and_bound_stack.append((node.right,node.val,float('inf')))

    return True


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

print(validateBST(root))


