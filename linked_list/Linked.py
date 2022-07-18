class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


# Basic api for linked list problemms are SEARCH, INSERT, DELETE Insert at Begining, Insert at End,
# Insert at Mid, Insert at a Position Delete first node, Delete last Node, Delete at a Position
# Reverse, Get the length, Print data in linked list
class LinkedList:
    def __init__(self, node=None) -> None:
        self.head: ListNode
        self.head = node
        if node != None:
            self.length = 1
        else:
            self.length = 0

    def insert_at_beginning(self, data):
        new_node = ListNode(data=data)
        if self.length == 0:
            self.head = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def insert_at_end(self, data):
        new_node = ListNode(data=data)
        if self.head is None:
            self.head = new_node
            self.length += 1
        current_node = self.head
        while True:
            if current_node.next is None:
                break
            current_node = current_node.next
        current_node.next = new_node
        self.length += 1

    def print_list(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next

    def length_list(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.next
        print(f"lenngth od lined list is {count}")

    def deleteLastNode(self):
        currentNode = self.head
        while currentNode.next:
            prevNode = currentNode
            currentNode = currentNode.next
        prevNode.next = None
        self.length -= 1

    def deleteKthLast(self, kth):
        dummy_head = ListNode(0, self.head)
        # 1 2 3 4 5 6 7 8 9
        first = dummy_head.next
        for _ in range(kth):
            first = first.next

        second = dummy_head
        while first:
            first, second = first.next, second.next
        second.next = second.next.next
        return dummy_head.next

    def remove_duplicates(self, L):
        it = L
        while it:
            next_distinct = it.next
            while next_distinct and next_distinct.data == it.data:
                next_distinct = next_distinct.next
            it.next = next_distinct
            it = next_distinct
        return L

    def print_linked_list_in_reverse(self, head):
        nodes = []
        while head:
            nodes.append(head.data)
            head = head.next
        while nodes:
            print(nodes.pop())
"""Brute force for reverse using recursion"""
def reverse(node):
    #_reverse() reverses and returns both head and tail.
    #Conventionally, an underscore denotes an unused variable.
    head,_= _reverse(node)
    return head

def _reverse(node):
    if node is None:
        return None, None
    if node.next is None:
        return node,node
    head, tail= _reverse(node.next)
    node.next = None
    tail.next = node
    return head, node

def search_list(L: LinkedList, key):
    while L and L.head.data != key:
        L = L.head.next
    return L

# Inser new_node after node


def insert_after(node: ListNode, new_node: ListNode):
    new_node.next = node.next
    node.next = new_node

# DeTete the node past this one. i{ssume node is not a taiT


def delete_after(node):
    node.next = node.next.next

def add_two_linked_list_thatt_represent_numbers(node0, node1, carry=0):
    if not node0 and not node1 and not carry:
        return None
    node0_val = node0.data if node0 else 0
    node1_val = node1.data if node1 else 0
    total = node0_val + node1_val + carry
    node0_next = node0.next if node0 else None
    node1_next = node1.next if node1 else None
    carry_next = 1 if total>= 10 else 0
    return ListNode(total % 10, add_two_linked_list_thatt_represent_numbers(node0_next, node1_next, carry_next))




node = ListNode(1)
l = LinkedList(node)
# l.insert_at_beginning(0)
l.insert_at_end(2)
l.insert_at_end(3)
l.insert_at_end(4)
l.insert_at_end(5)
l.insert_at_end(6)
l.insert_at_end(7)
l.insert_at_end(8)
l.insert_at_end(9)
l.print_linked_list_in_reverse(node)
# l.length_list()
