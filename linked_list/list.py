class Node:
    # constructor
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next
    # method for etting data field of the node

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next != None


class LinkedList():
    def __init__(self, node=None) -> None:
        self.head = node
        if node != None:
            self.length = 1
        else:
            self.length = 0

    def insert_atBeginning(self, data):
        newNode = Node()
        newNode.data = data
        if self.length == 0:
            self.head = newNode
            self.length += 1
        else:
            newNode.next = self.head
            self.head = newNode
            self.length += 1

    def insertAtBegining(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.length += 1
        else:
            currentNode = self.head
            self.head = node
            node.next = currentNode
            self.length += 1

    def insertAtEnd(self, data):
        newNode = Node(data=data)
        currentNode = self.head
        while True:
            if currentNode.next is None:
                break
            currentNode = currentNode.next
        currentNode.next = newNode
        self.length += 1

    def insert(self, newNode: Node):
        if self.head is None:
            self.head = newNode
            self.length += 1
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
            self.length += 1

    def print_list(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

    def length_list(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.next
        return count

    def insertAtMid(self, data):
        length = self.length
        newNode = Node(data)
        mid = length // 2
        currentNode = self.head
        for i in range(mid-1):
            currentNode = currentNode.next
            nextNode = currentNode.next
        currentNode.next = newNode
        currentNode.next.next = nextNode
        self.length += 1

    def insertAtPos(self, data, pos):
        length = self.length
        pos = pos
        newNode = Node(data)
        if pos > length or pos < 0:
            return None
        else:
            if pos == 0:
                self.insertAtBegining(data)
            else:
                currentNode = self.head
                for i in range(pos):
                    prevNode = currentNode
                    currentNode = currentNode.next
                prevNode.next = newNode
                newNode.next = currentNode
                self.length += 1

    def getlength(self):
        count = 0
        currentNode = self.head
        while currentNode:
            count += 1
            currentNode = currentNode.next
        print("Length from method is %s " % (count))

    def deleteFirstNode(self):
        currentNode = self.head
        nextNode = currentNode.next
        self.head = nextNode
        self.length -= 1

    def deleteFirstNode_2(self):
        if self.length == 0:
            print("The lis is Empty")
        else:
            self.head = self.head.next
            self.length -= 1

    def deleteLastNode(self):
        currentNode = self.head
        while currentNode.next:
            prevNode = currentNode
            currentNode = currentNode.next
        prevNode.next = None
        self.length -= 1

    def reverseList(self):
        current = self.head
        prev = None
        while current is not None:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        self.head = prev


node = Node(1)
l = LinkedList(node)
node = Node(2)
l.insert(node)
node = Node(3)
l.insert(node)
node = Node(4)
l.insert(node)
node = Node(5)
l.insert(node)
node = Node(6)
# l.insert(node)
# l.insertAtEnd(7)
# l.insertAtEnd(8)
# l.insertAtMid(10)
# l.insertAtPos(11, 0)
# l.insertAtPos(12, 1)
# l.print_list()
# print(f'The length of the linked list is {l.length}')
# l.deleteLastNode()
# print("Node Deleted \n")
# l.getlength()
# print("\n")
l.print_list()
l.reverseList()
print(".....................................................................................")
l.print_list()

# print(l.length_list())
