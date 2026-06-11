'''Problem Statement
A library stores book information in books.txt.
File Format
B101,Python Basics,5
B102,Java Programming,2
B103,Data Science,0 
B104,DBMS,3 
B105,Machine Learning,1
B106,Operating Systems,4 
B107,Networking,2 
B108,Cyber Security,6 
B109,Cloud Computing,0 
B110,Web Development,3
Requirements
Develop a program to:
1. Display all books.
2. Search a book using Book ID.
3. Issue a book (decrease quantity by 1).
4. Return a book (increase quantity by 1).
5. Display unavailable books.
6. Display books requiring restocking (copies < 2).
7. Update the file after every issue/return operation.
'''
#--------------------------------------------------------
# Function to load books from file into dictionary
#--------------------------------------------------------
def load_books():
    
    books = {}
    file = open("books.txt", "r")
    lines = file.readlines()
    for line in lines:
        data = line.strip().split(",")
        books[data[0]] = {
            "title": data[1],
            "qty": int(data[2])
        }
    file.close()

    return books

#--------------------------------------------------------
# Function to save updated records back to file
#--------------------------------------------------------

def save_books(books):
    file = open("books.txt", "w")
    for book_id in books:

        file.write(
            f"{book_id},{books[book_id]['title']},{books[book_id]['qty']}\n"
        )
    file.close()

#--------------------------------------------------------
# Function to display all books
#--------------------------------------------------------
def display_books(books):

    print("\n----- ALL BOOKS -----")

    print("Book ID\tTitle\t\t\tCopies")

    for book_id in books:
        print(book_id,
              "\t",
              books[book_id]["title"],
              "\t",
              books[book_id]["qty"])

#--------------------------------------------------------
# Function to search a book using Book ID
#--------------------------------------------------------
def search_book(books):

    # Take Book ID from user
    book_id = input("Enter Book ID : ")

    # Check if book exists
    if book_id in books:

        print("\nBook Found")
        print("Book ID :", book_id)
        print("Title   :", books[book_id]["title"])
        print("Copies  :", books[book_id]["qty"])

    else:
        print("Book not found.")

#--------------------------------------------------------
# Function to issue a book
#--------------------------------------------------------
def issue_book(books):
    book_id = input("Enter Book ID to Issue : ")
    if book_id in books:

        if books[book_id]["qty"] > 0:
            books[book_id]["qty"] -= 1
            save_books(books)

            print("Book Issued Successfully.")

        else:
            print("Book is unavailable.")

    else:
        print("Invalid Book ID.")

#--------------------------------------------------------
# Function to return a book
#--------------------------------------------------------
def return_book(books):
    book_id = input("Enter Book ID to Return : ")
    if book_id in books:
        books[book_id]["qty"] += 1
        save_books(books)

        print("Book Returned Successfully.")

    else:
        print("Invalid Book ID.")

#--------------------------------------------------------
# Function to display unavailable books
#--------------------------------------------------------
def unavailable_books(books):

    print("\n----- UNAVAILABLE BOOKS -----")

    found = False

    for book_id in books:

        if books[book_id]["qty"] == 0:

            print(book_id, "-", books[book_id]["title"])

            found = True

    if found == False:
        print("No unavailable books.")

#--------------------------------------------------------
# Function to display books needing restocking
#--------------------------------------------------------
def restock_books(books):

    print("\n----- BOOKS REQUIRING RESTOCK -----")

    found = False

    for book_id in books:

        if books[book_id]["qty"] < 2:

            print(book_id,
                  "-",
                  books[book_id]["title"],
                  "- Copies:",
                  books[book_id]["qty"])

            found = True

    if found == False:
        print("No books require restocking.")


# ------------------------------------------
# Main Program
# ------------------------------------------

while True:

    books = load_books()

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Display All Books")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Unavailable Books")
    print("6. Display Books Requiring Restocking")
    print("7. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        display_books(books)

    elif choice == "2":
        search_book(books)

    elif choice == "3":
        issue_book(books)

    elif choice == "4":
        return_book(books)

    elif choice == "5":
        unavailable_books(books)

    elif choice == "6":
        restock_books(books)

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")