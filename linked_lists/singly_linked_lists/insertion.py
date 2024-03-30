class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_position(self, position, value):
        if position <= 0:
            print("Invalid position")
            return

        if position == 1: #at the beginning
            self.insert_at_beginning(value)
            return

        new_node = Node(value)
        current = self.head
        count = 1

        # keep iterating until before the position
        while current and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print("Invalid position")
            return
        
        # before the position, add the node
        new_node.next = current.next

        # if there's anything that comes after the position, it should be the next of the node
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        new_node.prev = current


# Example usage:
linked_list = SinglyLinkedList()

# Insertion
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_beginning(5)
linked_list.insert_at_position(2, 15)
