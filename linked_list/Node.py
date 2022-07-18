# Node of a singly linked list
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node
        self.head = None

    def insert(self, newNode: Node):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def insertAtBegining(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            currentNode = self.head
            self.head = node
            node.next = currentNode

    def reverseList(self):
        # 1-> 2 -> 3 -> null
        prev = None
        current = self.head
        next_element = None
        while current:
            next_element = current.next
            current.next = prev
            prev = current
            current = next_element
        return prev

    def print_list(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

    def print_reverse_list(self, Node):
        currentNode = Node
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

    def reverseList(self):
        # 1-> 2 -> 3 -> null
        prev = None
        current = self.head
        while current:
            current_next = current.next
            current.next = prev
            prev = current
            current = current_next
        return prev



node = Node(1)
linkedlist = LinkedList()
linkedlist.insert(node)
node = Node(2)
linkedlist.insert(node)
node = Node(3)
linkedlist.insert(node)
node = Node(4)
linkedlist.insert(node)
# linkedlist.insertAtBegining(10)
# linkedlist.insertAtBegining(50)
linkedlist.print_list()

x = linkedlist.reverseList()
linkedlist.print_reverse_list(node)
