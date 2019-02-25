 # You have two numbers represented by a linked list, where each node contains a single digit.
# The digits are stored in reverse order, such that the 1 's digit is at the head of the list.
# Write a function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE Input: (7-) 1 -) 6) + (5 -) 9 -) 2).Thatis,617 + 295.
# Output: 2 -) 1 -) 9. That is, 912.
# FOLLOW UP Suppose the digits are stored in forward order.
# Repeat the above problem. EXAMPLE Input: (6 -) 1 -) 7) + (2 -) 9


class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def sumList(head1,head2):
    p = head1
    q = head2
    dummy = ListNode(None)
    curr = dummy
    carry = 0

    while p or q:
        if p is None:
            x = 0
        else :
            x = p.val
        if q is None:
            y = 0
        else:
            y = q.val
        sum_ = x+y+carry
        carry = sum_ /10
        curr.next = ListNode(sum_%10)
        curr = curr.next
        p = p.next
        q = q.next
    if carry > 0:
        curr.next = ListNode(carry)
        curr.next.next = None
    return dummy.next

def listTraverse(head):
    current = head
    while current:
        print(str(current.val) + '->'),
        current = current.next
    print None


a = ListNode(4)
b = ListNode(2)
c = ListNode(6)
d = ListNode(3)
e = ListNode(2)
f = ListNode(5)

a.next = b
b.next = c
c.next = None

d.next = e
e.next = f
f.next = None

head1 = a
head2 = d
print("Original Lists:")
listTraverse(head1)
listTraverse(head2)

sums_head = sumList(head1,head2)
print("Sum Lists:")
listTraverse(sums_head)
