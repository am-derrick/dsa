class MyList:
    def __init__(self):
        self.data = []

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


# Example usage:
my_list = MyList()

my_list.delete_at_end()
my_list.delete_at_beginning()
my_list.delete_at_index(1)
