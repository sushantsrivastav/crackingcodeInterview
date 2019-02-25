## Binary Tree traversal

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.val),
            self.inorder(node.right)

    def preorder(self,node):
        if node:
            print(node.val),
            self.preorder(node.left)
            self.postorder(node.right)

    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val),

a = TreeNode(10)
b = TreeNode(5)
c = TreeNode(20)
d = TreeNode(9)
e = TreeNode(18)
f = TreeNode(3)
g = TreeNode(7)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
root = a
print("####Inorder####")
a.inorder(a)
print("####postorder####")
a.postorder(a)
print("####preorder####")
a.preorder(a)

