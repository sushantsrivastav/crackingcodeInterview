#Stream: Imagine you are reading in a stream of integers.
# Periodically, you wish to be able to look up the rank of a number x (the number of values less than or equal to x).
#  Implement the data structures and algorithms to support these operations.
# That is, implement the method track (int x), which is called when each number is generated,
# and the method getRankOfNumber(int x), which returns the number of values less than or equal to X
# (not including x itself).
# EXAMPLE Stream(inorderofappearance):5, 1,4,4, 5, 9, 7, 13, 3
#  getRankOfNumber(l) 0
# getRankOfNumber(3) 1
# getRankOfNumber(4) 3

class TreeNode(object):
    def __init__(self,data,left_count=0):
        self.data = data
        self.left_count = left_count
        self.left = None
        self.right = None

class BST(object):
    def __init__(self,root= None):
        self.root = root

    def track(self,data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self.root = self._track(self.root,data)

    def _track(self,x,data):
        if x is None:
            return TreeNode(data)
        if data <= x.data:
            x.left = self._track(x.left,data)
            x.left_count += 1
        else:
            x.right = self._track(x.right,data)
        return x

    def get_rank_of_number(self,data):
        if self.root is None:
            return 0
        return self._get_rank_of_number(self.root,data)

    def _get_rank_of_number(self,x,data):
        if x is None:
            return None
        if data == x.data :
            return x.left_count
        elif data < x.data:
            return self._get_rank_of_number(x.left,data)
        else:
            right_count = self._get_rank_of_number(x.right,data)
            if right_count is None:
                return None
            return right_count + x.left_count + 1




bst = BST()
stream = [ 5, 1, 4, 4, 5, 9, 7, 13, 3 ]
for data in stream:
    bst.track(data)
print(bst.get_rank_of_number(4))
print(bst.get_rank_of_number(5))

