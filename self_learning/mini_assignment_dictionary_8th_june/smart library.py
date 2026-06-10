"""
Program: Digital Library Management System

Requirements:
1. Add a book
2. Remove a book
3. Search book by ID
4. Search book by Title
5. Update available copies
6. Issue a book
7. Return a book
8. Display books with fewer than 3 copies
9. Display unavailable books
10. Find most available book
11. Generate restocking report
12. Create separate dictionary of books requiring immediate purchase
13. Complete library summary report
"""

# Library Dictionary (30 Books) 

library = {
    "B101": {"title": "Python Basics", "author": "ABC", "copies": 5},
    "B102": {"title": "Data Structures", "author": "John", "copies": 4},
    "B103": {"title": "Algorithms", "author": "David", "copies": 2},
    "B104": {"title": "Machine Learning", "author": "Smith", "copies": 7},
    "B105": {"title": "Artificial Intelligence", "author": "Brown", "copies": 1},
    "B106": {"title": "Web Development", "author": "James", "copies": 6},
    "B107": {"title": "Database Systems", "author": "Martin", "copies": 3},
    "B108": {"title": "Computer Networks", "author": "Clark", "copies": 2},
    "B109": {"title": "Operating Systems", "author": "Miller", "copies": 4},
    "B110": {"title": "Cyber Security", "author": "Wilson", "copies": 1},
    "B111": {"title": "Cloud Computing", "author": "Taylor", "copies": 5},
    "B112": {"title": "Big Data", "author": "Thomas", "copies": 2},
    "B113": {"title": "Java Programming", "author": "Lee", "copies": 6},
    "B114": {"title": "C Programming", "author": "White", "copies": 8},
    "B115": {"title": "C++ Programming", "author": "Walker", "copies": 4},
    "B116": {"title": "JavaScript", "author": "Hall", "copies": 2},
    "B117": {"title": "HTML & CSS", "author": "Allen", "copies": 3},
    "B118": {"title": "React JS", "author": "Young", "copies": 1},
    "B119": {"title": "Node JS", "author": "King", "copies": 5},
    "B120": {"title": "Software Engineering", "author": "Scott", "copies": 4},
    "B121": {"title": "Computer Graphics", "author": "Green", "copies": 2},
    "B122": {"title": "Compiler Design", "author": "Adams", "copies": 3},
    "B123": {"title": "Linux Fundamentals", "author": "Baker", "copies": 6},
    "B124": {"title": "Android Development", "author": "Nelson", "copies": 2},
    "B125": {"title": "Data Science", "author": "Carter", "copies": 7},
    "B126": {"title": "Blockchain", "author": "Perez", "copies": 1},
    "B127": {"title": "Internet of Things", "author": "Roberts", "copies": 4},
    "B128": {"title": "Deep Learning", "author": "Turner", "copies": 5},
    "B129": {"title": "Ethical Hacking", "author": "Phillips", "copies": 2},
    "B130": {"title": "Digital Marketing", "author": "Campbell", "copies": 3}
}
# Functions 
#----------------------------------------------------
# Display all books
def display_books():
    print("\n----- Library Books -----")
    for bid, details in library.items():
        print(bid, ":", details)

#----------------------------------------------------
# Add a new book
def add_book():
    bid = input("Enter Book ID: ")

    if bid in library:
        print("Book ID already exists.")
    else:
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        copies = int(input("Enter Copies: "))

        library[bid] = {
            "title": title,
            "author": author,
            "copies": copies
        }

        print("Book Added Successfully.")

#----------------------------------------------------
# Remove a book
def remove_book():
    bid = input("Enter Book ID to remove: ")

    if bid in library:
        del library[bid]
        print("Book Removed Successfully.")
    else:
        print("Book Not Found.")

#----------------------------------------------------
# Search book by ID
def search_by_id():
    bid = input("Enter Book ID: ")

    if bid in library:
        print(library[bid])
    else:
        print("Book Not Found.")

#----------------------------------------------------
# Search by title
def search_by_title():
    title = input("Enter Book Title: ").lower()

    found = False

    for bid, details in library.items():
        if details["title"].lower() == title:
            print(bid, ":", details)
            found = True

    if not found:
        print("Book Not Found.")

#----------------------------------------------------
# Update copies
def update_copies():
    bid = input("Enter Book ID: ")

    if bid in library:
        new_copies = int(input("Enter New Copies: "))
        library[bid]["copies"] = new_copies
        print("Copies Updated.")
    else:
        print("Book Not Found.")

#----------------------------------------------------
# Issue a book
def issue_book():
    bid = input("Enter Book ID: ")

    if bid in library:
        if library[bid]["copies"] > 0:
            library[bid]["copies"] -= 1
            print("Book Issued Successfully.")
        else:
            print("Book Not Available.")
    else:
        print("Book Not Found.")

#----------------------------------------------------
# Return a book
def return_book():
    bid = input("Enter Book ID: ")

    if bid in library:
        library[bid]["copies"] += 1
        print("Book Returned Successfully.")
    else:
        print("Book Not Found.")

#----------------------------------------------------
# Books with fewer than 3 copies
def low_stock_books():
    print("\nBooks with Less Than 3 Copies")

    for bid, details in library.items():
        if details["copies"] < 3:
            print(bid, ":", details)

#----------------------------------------------------
# Unavailable books
def unavailable_books():
    print("\nUnavailable Books")

    found = False

    for bid, details in library.items():
        if details["copies"] == 0:
            print(bid, ":", details)
            found = True

    if not found:
        print("No unavailable books.")

#----------------------------------------------------
# Most available book
def most_available_book():
    max_book = max(library, key=lambda x: library[x]["copies"])

    print("\nMost Available Book")
    print(max_book, ":", library[max_book])

#----------------------------------------------------
# Restocking report
def restocking_report():
    print("\nRestocking Report (Copies < 3)")

    for bid, details in library.items():
        if details["copies"] < 3:
            print(bid, ":", details)

#----------------------------------------------------
# Immediate purchase dictionary
def immediate_purchase():
    purchase_dict = {}

    for bid, details in library.items():
        if details["copies"] <= 1:
            purchase_dict[bid] = details

    print("\nBooks Requiring Immediate Purchase")
    print(purchase_dict)

#----------------------------------------------------
# Library summary report
def library_summary():
    total_books = len(library)
    total_copies = 0

    for details in library.values():
        total_copies += details["copies"]

    print("\n===== LIBRARY SUMMARY REPORT =====")
    print("Total Different Books :", total_books)
    print("Total Copies Available :", total_copies)

    print("\nBooks with Low Stock (<3)")
    low_stock_books()

    print("\nMost Available Book")
    most_available_book()

    print("\nImmediate Purchase List")
    immediate_purchase()

#  Menu Driven Program 
#----------------------------------------------------
while True:

    print("\n===== DIGITAL LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Display All Books")
    print("2. Add Book")
    print("3. Remove Book")
    print("4. Search Book by ID")
    print("5. Search Book by Title")
    print("6. Update Copies")
    print("7. Issue Book")
    print("8. Return Book")
    print("9. Display Books with Less Than 3 Copies")
    print("10. Display Unavailable Books")
    print("11. Most Available Book")
    print("12. Restocking Report")
    print("13. Immediate Purchase Dictionary")
    print("14. Library Summary Report")
    print("15. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_books()

    elif choice == 2:
        add_book()

    elif choice == 3:
        remove_book()

    elif choice == 4:
        search_by_id()

    elif choice == 5:
        search_by_title()

    elif choice == 6:
        update_copies()

    elif choice == 7:
        issue_book()

    elif choice == 8:
        return_book()

    elif choice == 9:
        low_stock_books()

    elif choice == 10:
        unavailable_books()

    elif choice == 11:
        most_available_book()

    elif choice == 12:
        restocking_report()

    elif choice == 13:
        immediate_purchase()

    elif choice == 14:
        library_summary()

    elif choice == 15:
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")