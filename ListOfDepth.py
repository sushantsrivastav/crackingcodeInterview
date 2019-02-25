#Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth
# (e.g., if you have a tree with depth 0, you'll have 0 linked lists).

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def listDepth(root):
    if root is None:
        return None
    stack = [root]
    link_list_head = []
    while stack:
        dummy = ListNode(None)
        curr = dummy
        for i in range(len(stack)):
            node = stack.pop(0)
            curr.next = ListNode(node.val)
            curr = curr.next
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        link_list_head.append(dummy.next)

    return link_list_head


##Print linkedlist for validation##
def linkedListprint(link_list_head):
    for i in range(len(link_list_head)):
        head = link_list_head[i]
        while head :
            if head.next is None:
                print(head.val)
            else :
                print (head.val),
            head = head.next

###Create Tree##

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

link_list_head = listDepth(root)
linkedListprint(link_list_head)
