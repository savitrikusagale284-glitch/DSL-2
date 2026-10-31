class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)

        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def find_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Case 1: no left child
            if root.left is None:
                return root.right
            # Case 2: no right child
            if root.right is None:
                return root.left

            # Case 3: two children - use inorder successor
            successor = self.find_min(root.right)
            root.key = successor.key
            root.right = self.delete(root.right, successor.key)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")


bst = BinarySearchTree()

while True:
    print("\\n1. Insert  2. Search  3. Delete")
    print("4. Inorder  5. Preorder  6. Postorder  7. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        key = int(input("Enter value: "))
        bst.root = bst.insert(bst.root, key)

    elif choice == "2":
        key = int(input("Enter value to search: "))
        if bst.search(bst.root, key):
            print("Value found.")
        else:
            print("Value not found.")

    elif choice == "3":
        key = int(input("Enter value to delete: "))
        bst.root = bst.delete(bst.root, key)
        print("Deletion operation completed.")

    elif choice == "4":
        print("Inorder:", end=" ")
        bst.inorder(bst.root)
        print()

    elif choice == "5":
        print("Preorder:", end=" ")
        bst.preorder(bst.root)
        print()

    elif choice == "6":
        print("Postorder:", end=" ")
        bst.postorder(bst.root)
        print()

    elif choice == "7":
        break
    else:
        print("Invalid choice.")
