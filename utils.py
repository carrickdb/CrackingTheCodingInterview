class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def createLL(vals):
    head = Node(0)
    curr = head
    for i in vals:
        curr.next = Node(i)
        curr = curr.next
    return head.next

def printLL(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()