#You are given a binary tree in which each node contains an integer value (which might be positive or negative).
#  Design an algorithm to count the number of paths that sum to a given value. The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).


class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

##Brute Force
#time O(n logn)

def countPathSum(root,val):
    if root is None:
        return 0
    pathfromroot = countPathFromNode(root,0,val)
    pathonleft = countPathSum(root.left,val)
    pathonright = countPathSum(root.right,val)
    return pathfromroot + pathonleft + pathonright

def countPathFromNode(node,currentsum,targetsum):
    if node is None:
        return 0
    currentsum += node.val
    total_path = 0
    if currentsum == targetsum:
        total_path += 1
    total_path += countPathFromNode(node.left,currentsum,targetsum)
    total_path += countPathFromNode(node.right,currentsum,targetsum)
    return total_path


###Optimized approach
# time :O(n)
# space :O(log n) - O(n)
def pathSum(root,val):
    if root is None:
        return 0
    sum_table  = {}
    return count_path_sum(root,0,val,sum_table)

def count_path_sum(node,running_sum,target_sum,sum_table):
    if node is None:
        return 0
    running_sum += node.val
    sum_table[running_sum] = sum_table.get(running_sum,0) + 1
    total_path = sum_table.get(running_sum-target_sum,0)
    total_path += count_path_sum(node.left,running_sum,target_sum,sum_table)
    total_path += count_path_sum(node.right,running_sum,target_sum,sum_table)
    sum_table[running_sum] -= 1
    return total_path


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.left = None
root.right.right = TreeNode(11)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.left = None
root.left.right.right = TreeNode(2)
    # root.right.left.left = None
    # root.right.left.right = None
root.right.right.left = None
root.right.right.right = None

print(pathSum(root, 8))
print(countPathSum(root,8))
