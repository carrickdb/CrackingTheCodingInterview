import utils

def get_loop_beginning(head):
    t,h = head, head
    while True:
        t = t.next
        h = h.next.next
        if t == h:
            break
    p = head
    while p != t:
        p = p.next
        t = t.next
    return t


head = utils.createLL(["A", "B", "C", "D", "E"])
curr = head
c = None
while curr.next:
    if curr.val == "C":
        c = curr
    curr = curr.next
curr.next = c

curr = head
for _ in range(6):
    print(curr.val)
    curr = curr.next


print(get_loop_beginning(head).val)