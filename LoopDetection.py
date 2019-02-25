# Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.
# DEFINITION Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node,
# so as to make a loop in the linked list.
# EXAMPLE Input: A -) B -) C -) 0 -) E - ) C[thesameCasearlierl
# Output: C

class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def isLoop(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(3)
e = ListNode(2)
f = ListNode(1)
a.next = b
b.next = c
c.next = f
d.next = e
e.next = f
f.next = c
head = a
print(isLoop(head))

