class TextEditor:
    def __init__(self):
        self.document = ""
        self.undo_stack = []
        self.redo_stack = []

    def make_change(self, new_text):
        # Save current document before changing it.
        self.undo_stack.append(self.document)
        self.document += new_text

        # A new change clears the redo history.
        self.redo_stack.clear()
        print("Change added.")

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return

        self.redo_stack.append(self.document)
        self.document = self.undo_stack.pop()
        print("Undo successful.")

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo.")
            return

        self.undo_stack.append(self.document)
        self.document = self.redo_stack.pop()
        print("Redo successful.")

    def display(self):
        print("Current document:", self.document)


editor = TextEditor()

while True:
    print("\\n1. Make Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display Document")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        text = input("Enter text to add: ")
        editor.make_change(text)
    elif choice == "2":
        editor.undo()
    elif choice == "3":
        editor.redo()
    elif choice == "4":
        editor.display()
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
