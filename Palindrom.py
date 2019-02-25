#Implement a function to check if a linked list is a palindrome.

class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def reverse(head):
    current = head
    prev = None
    while current:
        temp  = current.next
        current.next = prev
        prev = current
        current = temp
    head = prev
    return head

def palindrom(head):
    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = reverse(slow.next)
    else:
        if slow.val != prev.val:
            return False
        slow = reverse(slow)
    fast = head

    while slow:
        if slow.val != fast.val:
            return False
        slow = slow.next
        fast = fast.next
    return True


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(3)
e = ListNode(2)
f = ListNode(1)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = None
head = a
print(palindrom(head))

