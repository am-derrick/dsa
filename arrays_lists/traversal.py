class MyList:
    def __init__(self):
        self.data = []

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

print("Accessing element at index 2:", my_list.access_at_index(2))
print("Traversing the list:")
my_list.traverse()
