
import re


class Stack:
    def __init__(self):
        self.items = []

    # new mehod for pushing an item on stack
    def push(self, item):
        self.items.append(item)

    # method for poping an ite from a stack
    def pop(self):
        return self.items.pop()

    # method for checkiing whether a stack is empty or not
    def isEmpty(self):
        return (self.items == [])

    # mehod to get the top of he stack
    def peek(self):
        return self.items[-1]

    def __str__(self) -> str:
        return str(self.items)


def infixToPostfix(infixexpr: str):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
        while not opStack.isEmpty():
            postfixList.append(opStack.pop())
        return " ".join(postfixList)


# x = "fdhjdk"
# print(x.split())
