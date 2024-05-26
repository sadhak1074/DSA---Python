class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Linking nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Inserting at the end
new_node = Node(50)
head = node1
current = head

# Traverse to the end of the list
while current.next is not None:
    current = current.next
current.next = new_node

# Printing nodes
current = head  # Reset current to head to print the list
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print('None')
