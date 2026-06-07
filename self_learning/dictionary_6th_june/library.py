"""
Program: Library Book Availability

This program performs the following tasks:
1. Displays books that are currently unavailable.
2. Counts the number of available books.
3. Finds the book with the maximum copies.
4. Creates a list of books having less than 3 copies.
5. Calculates the total number of books available.
"""

# Dictionary containing book names and available copies
books = {
    "Python Basics": 5,
    "Data Structures": 0,
    "Machine Learning": 3,
    "Java Programming": 2,
    "DBMS": 0,
    "Operating Systems": 6,
    "Networking": 4,
    "Cloud Computing": 1,
    "Cyber Security": 0,
    "Web Development": 7
}

#------------------------------------------------
# Display books that are currently unavailable

print("Books currently unavailable:")

for book, copies in books.items():
    if copies == 0:
        print(book)

#---------------------------------------------
# Count the number of available books

available_count = 0

for copies in books.values():
    if copies > 0:
        available_count += 1

print("\nNumber of available books:", available_count)

#--------------------------------------
 # find the book with the maximum copies

max_book = max(books, key=books.get)

print("\nBook with maximum copies:")
print(max_book, ":", books[max_book])

#------------------------------------------------
 # create a list of books having less than 3 copies

few_copies = []

for book, copies in books.items():
    if copies < 3:
        few_copies.append(book)

print("\nBooks having less than 3 copies:")
print(few_copies)

#-------------------------------------------------
# calculate the total number of books available

total_books = sum(books.values())

print("\nTotal number of books available:", total_books)