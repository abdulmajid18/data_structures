class Stack:
    def __init__(self, items=[]) -> None:
        self.items = items

    def isEmpty(self):
        # return self.items == None
        return not self.items

    def pop(self):
        return self.items.pop()

    def push(self, data):
        self.items.append(data)

    def __repr__(self) -> str:
        return "Stack {0} ".format(self.items)


def reverseStack(stack):
    def reverseStackRecursive(stack: Stack, newStack=Stack()):
        if not stack.isEmpty():
            popped = stack.pop()
            newStack.push(popped)
            reverseStackRecursive(stack, newStack)
        return newStack
    return reverseStackRecursive(stack)


elements = [i for i in range(10)]
stack = Stack(elements)
print(stack)

ans = reverseStack(stack)
print(ans)
