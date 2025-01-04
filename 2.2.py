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

    def kthToLast(self, k):
        curr = self.root
        kBehind = None
        kAhead = 1
        while curr:
            curr = curr.next
            if kAhead == k:
                if not kBehind:
                    kBehind = self.root
                else:
                    kBehind = kBehind.next
            else:
                kAhead += 1
        return kBehind


ll = LinkedList(None)
arr = [1, 2, 3, 4]
for num in arr:
    ll.prependNode(Node(num))
ll.printList()
kth = ll.kthToLast(2)
if kth:
    print(kth.val)
else:
    print("None")
