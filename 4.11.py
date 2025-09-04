import random

class RandomBinTree:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.size = 1

    def get_random_node(self):
        choice = random.randint(0, self.size-1)
        total = 0
        if self.left:
            if choice < self.left.size:
                return self.left.get_random_node()
            total += self.left.size
        if total == choice:
            return self
        if not self.right:
            print(choice, self.size, self.val)
        return self.right.get_random_node()

    def insert(self, val):
        if val <= self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = RandomBinTree(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = RandomBinTree(val)
        self.size += 1


l = [30, 10, 15, 35, 5, 17, 7, 3]

t = RandomBinTree(20)
for val in l:
    t.insert(val)

# stack = [t]
# while stack:
#     curr = stack.pop()
#     print(curr.val, end=" ")
#     if curr.right:
#         stack.append(curr.right)
#     if curr.left:
#         stack.append(curr.left)
# print()
# print(t.size)

for _ in range(20):
    print(t.get_random_node().val)
