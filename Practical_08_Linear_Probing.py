class LinearProbingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.DELETED = "<DELETED>"

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)

        for step in range(self.size):
            position = (index + step) % self.size
            current = self.table[position]

            if current == key:
                print("Key already exists.")
                return
            if current is None or current == self.DELETED:
                self.table[position] = key
                print("Key inserted at index", position)
                return

        print("Hash table is full.")

    def search(self, key):
        index = self.hash_function(key)

        for step in range(self.size):
            position = (index + step) % self.size
            current = self.table[position]

            if current is None:
                return -1
            if current == key:
                return position

        return -1

    def delete(self, key):
        position = self.search(key)

        if position == -1:
            print("Key not found.")
        else:
            # A marker is needed so searches can continue past this slot.
            self.table[position] = self.DELETED
            print("Key deleted.")

    def display(self):
        for index, value in enumerate(self.table):
            print(index, ":", value)


ht = LinearProbingHashTable()

while True:
    print("\\n1. Insert  2. Search  3. Delete  4. Display  5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        key = int(input("Enter key: "))
        ht.insert(key)

    elif choice == "2":
        key = int(input("Enter key to search: "))
        position = ht.search(key)
        if position == -1:
            print("Key not found.")
        else:
            print("Key found at index", position)

    elif choice == "3":
        key = int(input("Enter key to delete: "))
        ht.delete(key)

    elif choice == "4":
        ht.display()

    elif choice == "5":
        break
    else:
        print("Invalid choice.")
