def partition(head, pv):
    second = None
    secondEnd = None
    dummy = Node(0)
    dummy.next = head
    curr = head
    prev = dummy
    while curr:
        if curr.val < pv:
            prev = curr
            curr = curr.next
        else:
            node = curr
            curr = curr.next
            prev.next = curr
            node.next = None
            if not second:
                second = node
                secondEnd = node
            else:
                secondEnd.next = node
                secondEnd = secondEnd.next
    prev.next = second
    return dummy.next

head = createLL([3,5,8,5,10,2,1])
printLL(head)
head = partition(head, 5)
printLL(head)

head = createLL([300,5,8,2,1])
printLL(head)
head = partition(head, 5)
printLL(head)

head = createLL([6,2,7])
printLL(head)
head = partition(head, 1)
printLL(head)

head = createLL([6,2,7])
printLL(head)
head = partition(head, 10)
printLL(head)