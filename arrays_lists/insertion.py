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


# Example usage:
my_list = MyList()

# Insertion
my_list.insert_at_end(10)
my_list.insert_at_end(20)
my_list.insert_at_beginning(5)
my_list.insert_at_index(2, 15)
