#Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binary search tree with minimal height.

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def sortedArrayToBST(nums):
    if nums == [] or nums == None :
            return None

    mid = len(nums)//2

    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[0:mid])
    root.right = sortedArrayToBST(nums[mid+1:])

    return root

def preOrder(node):
    if node:
        print(node.val),
        preOrder(node.left)
        preOrder(node.right)

nums = [1,5,8,9,15,20]
root = sortedArrayToBST(nums)
preOrder(root)
