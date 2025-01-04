from collections import deque


class SetOfStacks:

    def __init__(self, max_size):
        self.stacks = []
        self.max_size = max_size

    def push(self, val):
        if not self.stacks or len(self.stacks[-1]) >= self.max_size:
            self.stacks.append(deque())
        self.stacks[-1].append(val)

    def pop(self, val):
        if not self.stacks:
            raise Exception("trying to pop from an empty stack")
        ret = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return ret

    def printStacks(self):
        for stack in self.stacks:
            for item in stack:
                print(item, end=' ')
            print()
        print()

    def popAt(self, index):
        if len(self.stacks) - 1 < index:
            raise Exception("no stack at that index")
        ret = self.stacks[index].pop()
        if len(self.stacks[index]) == 0:
            del self.stacks[index]
        else:
            for i in range(index, len(self.stacks)-1):
                movedElement = self.stacks[i+1].popleft()
                self.stacks[i].append(movedElement)
            if len(self.stacks[-1]) == 0:
                self.stacks.pop()
        return ret

stack = SetOfStacks(3)
for i in range(20):
    stack.push(i)
stack.printStacks()
stack.popAt(3)
stack.printStacks()
stack.popAt(2)
stack.printStacks()
