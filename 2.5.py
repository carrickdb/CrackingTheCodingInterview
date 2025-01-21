import utils

# Part 1

# def addLL(h1, h2):
#     carry = 0
#     c1,c2 = h1,h2
#     newhead = None
#     curr = None
#     while c1 or c2:
#         total = carry
#         if c1:
#             total += c1.val
#             c1 = c1.next
#         if c2:
#             total += c2.val
#             c2 = c2.next
#         newNode = utils.Node(total%10)
#         if not newhead:
#             newhead = newNode
#         else:
#             curr.next = newNode
#         curr = newNode
#         carry = total//10
#     if carry:
#         curr.next = utils.Node(carry)
#     return newhead
#
#
# h1 = utils.createLL([1,2,3])
# h2 = utils.createLL([4,1,5])
# llsum = addLL(h1, h2)
# utils.printLL(llsum)
#
# h1 = utils.createLL([1])
# h2 = utils.createLL([9,9,9])
# llsum = addLL(h1, h2)
# utils.printLL(llsum)
#
# h1 = utils.createLL([7,8,2])
# h2 = utils.createLL([9,3])
# utils.printLL(h1)
# llsum = addLL(h1, h2)
# utils.printLL(llsum)


# Part 2

def addLL(h1, h2):
    carry = 0
    c1,c2 = h1,h2
    newhead = None
    curr = None
    while c1 or c2:
        total = carry
        if c1:
            total += c1.val
            c1 = c1.next
        if c2:
            total += c2.val
            c2 = c2.next
        newNode = utils.Node(total%10)
        if not newhead:
            newhead = newNode
        else:
            curr.next = newNode
        curr = newNode
        carry = total//10
    if carry:
        curr.next = utils.Node(carry)
    return newhead


h1 = utils.createLL([1,2,3])
h2 = utils.createLL([4,1,5])
llsum = addLL(h1, h2)
utils.printLL(llsum)

h1 = utils.createLL([1])
h2 = utils.createLL([9,9,9])
llsum = addLL(h1, h2)
utils.printLL(llsum)

h1 = utils.createLL([7,8,2])
h2 = utils.createLL([9,3])
utils.printLL(h1)
llsum = addLL(h1, h2)
utils.printLL(llsum)