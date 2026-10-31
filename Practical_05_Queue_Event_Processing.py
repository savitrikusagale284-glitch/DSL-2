from collections import deque


class EventQueue:
    def __init__(self):
        self.events = deque()

    def add_event(self, event):
        self.events.append(event)
        print("Event added.")

    def process_event(self):
        if not self.events:
            print("No pending events.")
        else:
            event = self.events.popleft()
            print("Processing event:", event)

    def display_events(self):
        if not self.events:
            print("No pending events.")
        else:
            print("Pending events:")
            for event in self.events:
                print(event)

    def cancel_event(self, event):
        try:
            self.events.remove(event)
            print("Event cancelled.")
        except ValueError:
            print("Event not found.")


queue = EventQueue()

while True:
    print("\\n1. Add Event")
    print("2. Process Next Event")
    print("3. Display Pending Events")
    print("4. Cancel Event")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        event = input("Enter event name: ")
        queue.add_event(event)
    elif choice == "2":
        queue.process_event()
    elif choice == "3":
        queue.display_events()
    elif choice == "4":
        event = input("Enter event name to cancel: ")
        queue.cancel_event(event)
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
