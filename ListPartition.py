class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def listPartition(node,x):
    head = node
    tail = node
    while node:
        next_node = node.next
        if node.val < x :
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = next_node
    tail.next = None
    return head


def listTraverse(head):
    current = head
    while current:
        print(str(current.val) + '->'),
        current = current.next
    print None


a = ListNode(3)
b = ListNode(5)
c = ListNode(8)
d = ListNode(5)
e = ListNode(10)
f = ListNode(2)
g = ListNode(1)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = None
head = a
print("Original List:")
listTraverse(head)
new_head = listPartition(head,5)
listTraverse(new_head)