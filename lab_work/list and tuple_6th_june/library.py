"""
Program: Library Book Analysis

This program performs the following tasks:
1. Display unavailable books.
2. Find all books with more than 2 copies.
3. Count available books.
4. Stop searching once a requested book is found.
"""

books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]

# --------------------------------------------------
# Task 1: Display unavailable books

print("Unavailable Books")

for book in books:
    title = book[0]
    copies = book[1]

    if copies == 0:
        print(title)

# --------------------------------------------------
# Task 2: Find all books with more than 2 copies

print("\nBooks With More Than 2 Copies")

for book in books:
    title = book[0]
    copies = book[1]

    if copies > 2:
        print(title, "-", copies, "copies")

# --------------------------------------------------
# Task 3: Count available books

available_books = 0

for book in books:
    if book[1] > 0:
        available_books += 1

print("\nNumber of Available Books :", available_books)

# --------------------------------------------------
# Task 4: Stop searching once a requested book is found

requested_book = "Java Programming"

for book in books:
    if book[0] == requested_book:
        print("\nBook Found :", book[0])
        print("Available Copies :", book[1])
        break