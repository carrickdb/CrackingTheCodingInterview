import math
def sortStack(stack):
    other = []
    while stack:
        curr = stack.pop()
        while other and other[-1] > curr:
            stack.append(other.pop())
        other.append(curr)
    while other:
        stack.append(other.pop())
    return stack

print(sortStack([7,2,21,7,2,4]))
print(sortStack([]))