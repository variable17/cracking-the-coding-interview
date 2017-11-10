"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if not head:
        return False
    else:
        (p,q) = (head, head)
        while q.next != None:
            p = p.next
            q = q.next.next
            if p == q:
                return True
        return False