class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def delMiddle(head):
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    if length % 2 == 0 :
        middle = length/2
    else:
        middle = (length/2) + 1
    print(middle)

    counter = 1
    prev = None
    current = head
    while counter < middle:
        prev = current
        current = current.next
        counter += 1
    prev.next = current.next


def listTraverse(head):
    current = head
    while current:
        print(str(current.val) + '->'),
        current = current.next
    print None

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = None
head = a
print("Original List:")
listTraverse(head)
delMiddle(head)
listTraverse(head)