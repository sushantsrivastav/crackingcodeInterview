#In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes
#  which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom
# (Le., each disk sits on top of an even larger one). You have the following constraints:
#  (1) Only one disk can be moved at a time.
# (2) A disk is slid off the top of one tower onto another tower.
# (3) A disk cannot be placed on top of a smaller disk.
# Write a program to move the disks from the first tower to the last using stacks.

class tower(object):
    def __init__(self,discs = None):
        if discs:
            self.discs = discs
        else:
            self.discs = []

def tower_of_hannoi(tower1,tower2,tower3,n = None):
    if n is None:
        n = len(tower1.discs)

    if n == 0:
        return

    tower_of_hannoi(tower1,tower3,tower2,n-1)
    tower3.discs.append(tower1.discs.pop())
    tower_of_hannoi(tower2,tower1,tower3,n-1)

tower1 = tower(["6", "5", "4", "3", "2", "1"])
tower2 = tower()
tower3 = tower()
print("###before move###")
print(tower1.discs)
print(tower2.discs)
print(tower3.discs)
tower_of_hannoi(tower1,tower2,tower3)
print('###After move###')
print(tower1.discs)
print(tower2.discs)
print(tower3.discs)
