class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Create the linked list and three nodes
linked_list = LinkedList()

# Create nodes
node1 = Node('Node 1')
node2 = Node('Node 2')
node3 = Node('Node 3')

# Link nodes
linked_list.head = node1
node1.next = node2
node2.next = node3

# Print the linked list
linked_list.print_list()
