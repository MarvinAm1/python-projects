# Initializing the Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Initializing the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

# Creating a method to add a node at the end of the linked list
    def append(self, data):
        new_node = Node(data)
        # Checks if there isn't a head node in the linked list and makes the new node the head (first) node
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        # Pushes over the first node added and connects the last node (which was originally first) with the new first node
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

# Creating a method that adds a node at the beginning of the linked list
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

# Creating a method that removes and deletes a node from the linked list
    def remove(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next
        if current_node.next:
            current_node.next = current_node.next.next

# Creating a method that displays and shows the entire linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Main() driver
# Creating an instance of the list
linked = LinkedList()

# Adding nodes into the list
linked.append(1)
linked.append(2)
linked.append(3)
linked.append(4)

# Displaying the entire list
linked.display()

# Adding a node at the beginning of the list
linked.prepend(0)
linked.display()

# Adding a node at the end of the list
linked.append(5)
linked.display()

# Removing a node from the list
linked.remove(4)
linked.display()



