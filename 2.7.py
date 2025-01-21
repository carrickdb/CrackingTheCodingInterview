import utils

def intersect(LL1, LL2):
    curr = LL1
    len1 = 0
    while curr:
        len1 += 1
        curr = curr.next
    len2 = 0
    curr = LL2
    while curr:
        len2 += 1
        curr = curr.next
    if len1 > len2:
        curr = LL1
        otherCurr = LL2
    else:
        otherCurr = LL1
        curr = LL2
    for i in range(abs(len1-len2)):
        curr = curr.next
    while otherCurr and curr:
        if otherCurr == curr:
            return True
        otherCurr = otherCurr.next
        curr = curr.next
    return False

ll = utils.createLL([1,2,3,4,5,6])
ll2 = utils.createLL([-1,-2,-3])
print(intersect(ll,ll2))

curr = ll2
while curr.next:
    curr = curr.next
curr.next = ll.next.next

print(intersect(ll,ll2))

print(intersect(None, None))