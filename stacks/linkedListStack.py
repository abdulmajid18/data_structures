class Node:
    # constcutoor
    def __init__(self, data=None,  next=None) -> None:
        self.data = data
        self.next = next

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, data):
        self.next = data

    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next != None


class Stack(object):
    def __init__(self, data=None):
        self.head = None
        if data:
            for data in data:
                self.push(data)

    def push(self, data):
        newNode = Node()
        newNode.data = data
        temphead = self.head
        self.head = newNode
        self.head.next = temphead

    def pop(self):
        if self.head is None:
            raise IndexError
        temp = self.head.data
        self.head = self.head.next
        return temp

    def peek(self):
        if self.head is None:
            raise IndexError
        return self.head.data


ourList = ["first", "second", "third"]  # , "fourth"]
ourStack = Stack(ourList)
print(ourStack.pop())
# print(ourStack.pop())
