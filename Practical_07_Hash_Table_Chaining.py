class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        # Update value if key already exists.
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                print("Value updated.")
                return

        self.table[index].append([key, value])
        print("Key-value pair inserted.")

    def search(self, key):
        index = self.hash_function(key)

        for stored_key, value in self.table[index]:
            if stored_key == key:
                return value
        return None

    def delete(self, key):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                print("Key deleted.")
                return

        print("Key not found.")

    def display(self):
        for index, chain in enumerate(self.table):
            print(index, ":", chain)


ht = HashTable()

while True:
    print("\\n1. Insert  2. Search  3. Delete  4. Display  5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        key = int(input("Enter key: "))
        value = input("Enter value: ")
        ht.insert(key, value)

    elif choice == "2":
        key = int(input("Enter key to search: "))
        result = ht.search(key)
        if result is None:
            print("Key not found.")
        else:
            print("Value:", result)

    elif choice == "3":
        key = int(input("Enter key to delete: "))
        ht.delete(key)

    elif choice == "4":
        ht.display()

    elif choice == "5":
        break
    else:
        print("Invalid choice.")
