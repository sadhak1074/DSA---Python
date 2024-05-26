class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#creating nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

#linking nodes
node1.next = node2
node2.next = node3
node3.next = node4

#Adding a new node at the beginning
current = node1
new_node = Node(50)
new_node.next = node1
current = new_node

#printing nodes
while current is not None:
    print(current.data, end = "->")
    current = current.next
print('None')
    