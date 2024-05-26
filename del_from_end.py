class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating nodes
head = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Linking nodes
head.next = node2
node2.next = node3
node3.next = node4

# Deleting node from the end
if head is not None:
    if head.next is None:
        head = None  # If there's only one node, set head to None
    else:
        current = head
        while current.next.next is not None:
            current = current.next
        current.next = None  # Set the next of the second-to-last node to None

# Printing nodes
current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print('None')
