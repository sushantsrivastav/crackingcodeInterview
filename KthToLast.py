# Implement an algorithm to find the kth to last element of a singly linked list.

class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def kthToLast(head,k):
    length = 0
    current = head
    while current:
        length += 1
        current = current.next

    print("length : " + str(length))

    l = length - k
    counter = 1
    current = head
    while counter <= l:
        current = current.next
        counter += 1
    print(current.val)


def listTraverse(head):
    current = head
    while current:
        print(str(current.val) + '->'),
        current = current.next
    print None

a = ListNode(1)
b = ListNode(2)
c = ListNode(2)
d = ListNode(2)
e = ListNode(3)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = None
head = a
print("Original List:")
listTraverse(head)
kthToLast(head,2)