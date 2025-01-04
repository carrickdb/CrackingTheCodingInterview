class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:

    def __init__(self, root):
        self.root = root

    def prependNode(self, node):
        node.next = self.root
        self.root = node

    def printList(self):
        curr = self.root
        while curr:
            print(curr.val, end=' ')
            curr = curr.next
        print()

    def removeDuplicates(self):
        curr = self.root
        while curr:
            otherCurr = curr
            while otherCurr and otherCurr.next:
                if otherCurr.next.val == curr.val:
                    otherCurr.next = otherCurr.next.next
                otherCurr = otherCurr.next
            curr = curr.next



ll = LinkedList(None)
arr = [1, 0, 1, 0, 2, 3, 4, 5, 1]
for num in arr:
    ll.prependNode(Node(num))

ll.printList()
ll.removeDuplicates()
ll.printList()
