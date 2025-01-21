import utils


def getLength(ll):
    total = 1
    while ll:
        total += 1
        ll = ll.next
    return total

def reverseLL(ll):
    curr = ll
    prev = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def checkPalindrome(head):
    length = getLength(head)
    other = None
    i = 0
    c = head
    while i < length//2:
        c = c.next
        i += 1
    if length % 2 == 1:
        other = c.next
    else:
        other = c
    other = reverseLL(other)
    c1,c2 = head, other
    while c1 and c2:
        if c1.val != c2.val:
            return False
        c1 = c1.next
        c2 = c2.next
    return True


head = utils.createLL(["a", "b", "c", "d", "e", "d", "c", "q", "a"])
head = reverseLL(head)
utils.printLL(head)

print(checkPalindrome(head))