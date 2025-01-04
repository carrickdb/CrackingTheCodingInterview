class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

    def printListFromNode(self):
        curr = self
        while curr:
            print(curr.val, end=' ')
            curr = curr.next
        print()

def deleteMiddleNode(node):
    node.val = node.next.val
    node.next = node.next.next


root = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
root.next = two
two.next = three
three.next = four
root.printListFromNode()
deleteMiddleNode(two)
root.printListFromNode()
