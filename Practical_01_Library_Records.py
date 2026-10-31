from collections import Counter

# Member ID : list of books borrowed by that member
library = {
    "M001": ["Python", "C"],
    "M002": ["Python"],
    "M003": [],
    "M004": ["Java", "Python"],
    "M005": ["C"],
    "M006": []
}

# 1. Average number of books borrowed by all members
total_members = len(library)
total_borrowed = sum(len(books) for books in library.values())

if total_members > 0:
    average = total_borrowed / total_members
    print("Average books borrowed:", average)
else:
    print("No library members found.")

# 2. Count how many times each book was borrowed
book_counts = Counter()
for books in library.values():
    book_counts.update(books)

if book_counts:
    highest_book = max(book_counts, key=book_counts.get)
    lowest_book = min(book_counts, key=book_counts.get)
    print("Most borrowed book:", highest_book, "-", book_counts[highest_book], "times")
    print("Least borrowed book:", lowest_book, "-", book_counts[lowest_book], "times")
else:
    print("No books have been borrowed.")

# 3. Count members who borrowed zero books
zero_members = sum(1 for books in library.values() if len(books) == 0)
print("Members with zero borrowings:", zero_members)

# 4. Mode of the number of books borrowed per member
borrow_counts = [len(books) for books in library.values()]
if borrow_counts:
    frequency = Counter(borrow_counts)
    highest_frequency = max(frequency.values())
    modes = [count for count, freq in frequency.items() if freq == highest_frequency]
    print("Mode of member borrow counts:", modes)
