#Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP How would you solve this problem if a temporary buffer is not allowed?

class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def delDuplicate(head):
    duplicate = set()
    current = head
    prev = None
    while current:
        if current.val in duplicate:
            prev.next = current.next
        else:
            duplicate.add(current.val)
            prev = current
        current = current.next



def delDuplicate2(head):
    current = head
    while current:
        runner = current
        while runner.next:
            if current.val == runner.next.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next


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
print("Afteer del duplicate:")
delDuplicate2(head)
listTraverse(head)






