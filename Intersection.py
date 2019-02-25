#Given two (singly) linked lists, determine if the two lists intersect.Return the intersecting node.
# Note that the intersection is defined based on reference, not value.
# That is, if the kth node of the first linked list is the exact same node (by reference) as
# the jth node of the second linked list, then they are intersecting.


class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def intersection(head1,head2):
    p = head1
    q = head2
    l1 = l2 = 0
    while p:
        l1 +=1
        p = p.next
    while q:
        l2 += 1
        q = q.next

    diff = abs(l1-l2)
    p = head1
    q = head2

    if l1 > l2:
        for i in range(diff):
            p = p.next
    if l2 > l1:
        for i in range(diff):
            q = q.next

    while p and q :
        if p == q:
            return p
        p = p.next
        q = q.next
    return None



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
e.next = c
f.next = None
head1 = a
head2 = d
print(intersection(head1,head2)==c)