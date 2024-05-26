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

def delete_node(head, key):
    # If the list is empty
    if head is None:
        return head

    # If the node to be deleted is the head node
    if head.data == key:
        return head.next

    # Find the node to be deleted
    current = head
    while current.next is not None:
        if current.next.data == key:
            break
        current = current.next

    # If the node was not found in the list
    if current.next is None:
        return head

    # Remove the node from the list
    current.next = current.next.next

    return head

# Delete a specific node (e.g., node with data 30)
head = delete_node(head, 30)

# Printing nodes
current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print('None')
