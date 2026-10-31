class Node:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.next = None


class StudentLinkedList:
    def __init__(self):
        self.head = None

    def add_student(self, roll_no, name, marks):
        if self.search_student(roll_no) is not None:
            print("Roll number already exists.")
            return

        new_node = Node(roll_no, name, marks)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

        print("Student added.")

    def search_student(self, roll_no):
        current = self.head
        while current is not None:
            if current.roll_no == roll_no:
                return current
            current = current.next
        return None

    def delete_student(self, roll_no):
        current = self.head
        previous = None

        while current is not None and current.roll_no != roll_no:
            previous = current
            current = current.next

        if current is None:
            print("Student not found.")
            return

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

        print("Student deleted.")

    def update_student(self, roll_no, name, marks):
        student = self.search_student(roll_no)
        if student is None:
            print("Student not found.")
        else:
            student.name = name
            student.marks = marks
            print("Student updated.")

    def display(self):
        current = self.head
        if current is None:
            print("No student records.")
            return

        while current is not None:
            print("Roll No:", current.roll_no,
                  "| Name:", current.name,
                  "| Marks:", current.marks)
            current = current.next

    def sort_students(self, key="marks", descending=False):
        records = []
        current = self.head

        while current is not None:
            records.append((current.roll_no, current.name, current.marks))
            current = current.next

        if key == "marks":
            records.sort(key=lambda record: record[2], reverse=descending)
        else:
            records.sort(key=lambda record: record[0], reverse=descending)

        for roll_no, name, marks in records:
            print("Roll No:", roll_no, "| Name:", name, "| Marks:", marks)


students = StudentLinkedList()

while True:
    print("\\n1. Add  2. Delete  3. Update  4. Search")
    print("5. Display  6. Sort  7. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        roll = int(input("Roll number: "))
        name = input("Name: ")
        marks = float(input("Marks: "))
        students.add_student(roll, name, marks)

    elif choice == "2":
        roll = int(input("Roll number to delete: "))
        students.delete_student(roll)

    elif choice == "3":
        roll = int(input("Roll number to update: "))
        name = input("New name: ")
        marks = float(input("New marks: "))
        students.update_student(roll, name, marks)

    elif choice == "4":
        roll = int(input("Roll number to search: "))
        student = students.search_student(roll)
        if student:
            print(student.roll_no, student.name, student.marks)
        else:
            print("Student not found.")

    elif choice == "5":
        students.display()

    elif choice == "6":
        key = input("Sort by marks or roll: ").lower()
        order = input("Ascending or descending? ").lower()
        students.sort_students(key, descending=(order == "descending"))

    elif choice == "7":
        break
    else:
        print("Invalid choice.")
