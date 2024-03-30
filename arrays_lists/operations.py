class MyList:
    def __init__(self):
        self.data = []
    
    # insertion functions
    def insert_at_beginning(self, value):
        self.data.insert(0, value)

    def insert_at_index(self, index, value):
        if index < 0 or index > len(self.data):
            print("Index out of bounds")
            return
        self.data.insert(index, value)

    def insert_at_end(self, value):
        self.data.append(value)

    # deletion functions
    def delete_at_beginning(self):
        if not self.data:
            print("List is empty")
            return
        self.data.pop(0)

    def delete_at_index(self, index):
        if index < 0 or index >= len(self.data):
            print("Index out of bounds")
            return
        self.data.pop(index)

    def delete_at_end(self):
        if not self.data:
            print("List is empty")
            return
        self.data.pop()

    def delete_item(self, value):
        self.data.remove(value)

    # access and traversal functions
    def access_at_index(self, index):
        self.data[index]

    def traverse(self):
        for item in self.data:
            print(item, end=" ")
        print

    """ other functions to consider
    list.clear()
    list.count(x)
    list.sort()
    list.index(x[, start[, end])
    """



# Example usage:
my_list = MyList()

# Insertion
my_list.insert_at_end(10)
my_list.insert_at_end(20)
my_list.insert_at_beginning(5)
my_list.insert_at_index(2, 15)

# Access and traversal
print("Accessing element at index 2:", my_list.access_at_index(2))
print("Traversing the list:")
my_list.traverse()

# Deletion
my_list.delete_at_end()
my_list.delete_at_beginning()
my_list.delete_at_index(1)

print("After deletion:")
my_list.traverse()
