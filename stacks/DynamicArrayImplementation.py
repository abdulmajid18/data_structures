import random


class Stack:
    def __init__(self, Capacity=1):
        self.top = -1
        self.Capacity = Capacity
        self.A = [None] * Capacity

    def push(self, data):
        if self.Capacity == self.top + 1:
            print("Trying to resize: Increase")
            self.resize()
        if self.isFull():
            print("Stack overflow")
            return
        self.top = self.top + 1
        self.A[self.top] = data

    def resize(self):
        self.Capacity = self.Capacity * 3
        newArray = [None] * self.Capacity
        if newArray is None:
            print(":( Use big machine")
            return
        for i in range(0, self.top+1):
            newArray[i] = self.A[i]
            self.A = newArray

    def pop(self):
        if self.top == -1:
            print("Stack underflow")
            return
        temp = self.A[self.top]
        self.top = self.top - 1
        if self.top < self.Capacity//2:
            print("Trying to resize: Decrease")
            self.Capacity = self.Capacity//2
            newArray = [None] * self.Capacity
            for i in range(0, self.top+1):
                newArray[i] = self.A[i]
            self.A = newArray
        return temp

    def peek(self):
        if self.top == -1:
            print("Stack underflow")
            return
        return self.A[self.top]

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.Capacity == self.top + 1


stack = Stack(Capacity=11)
for i in range(10):
    stack.push(random.randint(1, 21))
for x in range(12):
    temp = stack.pop()
    if temp is not None:
        print(temp)
