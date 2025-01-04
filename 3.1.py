class StackArray:

    def __init__(self, size):
        """
        initialize stack with size `size` with three pointers pointing to tops of each stack
        """
        self.stacks = [None for i in range(size)]
        self.stackPointers = [-1, -1, -1]
        self.starts = [0, size//3, size//3 * 2]

    def peek(self, stackNum):
        if self.stackPointers[stackNum] < 0:
            raise Exception("peek from empty stack")
        return self.stacks[self.stackPointers[stackNum]]

    def pop(self, stackNum):
        curr = self.stackPointers[stackNum]
        if curr < 0:
            raise Exception("pop from empty stack")
        ret = self.stacks[curr]
        self.stacks[curr] = None
        self.stackPointers[stackNum] -= 1
        if self.stackPointers[stackNum] < self.starts[stackNum]:
            self.stackPointers[stackNum] = -1
        return ret

    def push(self, stackNum, val):
        if stackNum == 2:
            if self.stackPointers[2] == len(self.stacks)-1:
                raise Exception("no more room!")
        elif self.stackPointers[stackNum] == self.starts[stackNum+1]-1:
            """
            get the remaining space.
            get secondStackFraction = secondStack/(secondStack+thirdStack) and similarly for the third stack
            allocate remainingSecondSpace = secondStackFraction*remainingSpace/2 to the second stack and similarly for the third stack
            Move the third stack first
            the stack pointer should end up at starts[2] - remainingSecondSpace
            for each element in the second stack, starting from the top:
                move this element to the new stack pointer
                decrement the stack pointer
            update the start position
            """
            raise Exception("no more room!")
        if self.stackPointers[stackNum] < 0:
            self.stackPointers[stackNum] = self.starts[stackNum]
        else:
            self.stackPointers[stackNum] += 1
        self.stacks[self.stackPointers[stackNum]] = val



stacks = StackArray(6)
# print(stacks.peek(1))
stacks.push(2, 3)
print(stacks.stacks)
print(stacks.peek(2))
stacks.push(2, 6)
print(stacks.stacks)
print(stacks.peek(2))
stacks.pop(2)
print(stacks.peek(2))
print(stacks.stacks)
# stacks.push(1,400)
# stacks.push(2, 9)
# stacks.pop(0)
