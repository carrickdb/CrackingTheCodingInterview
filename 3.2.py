"""
1
3
2

"""

class StackWithMin:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        if not self.minStack or val < self.minStack[-1]:
            self.minStack.append(val)

    def pop(self):
        top = self.stack.pop()
        if top == self.minStack[-1]:
            self.minStack.pop()

    def getMin(self):
        return self.minStack[-1]

s = StackWithMin()
s.push(2)
print(s.getMin())
s.push(3)
print(s.getMin())
s.push(1)
print(s.getMin())
s.pop()
print(s.getMin())
s.pop()
print(s.getMin())
