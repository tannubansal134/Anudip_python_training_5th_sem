'''Problem Statement
Create a digital library management system.
Example Structure
library = {
 "B101": { 
 "title": "Python Basics", 
 "author": "ABC", 
 "copies": 5 
 } 
 }
Maintain records of at least 30 books.
Requirements
1.Add a book.
2.Remove a book.
3.Search a book by ID.
4.Search by title.
5.Update available copies.
6.Issue a book.
7.Return a book.
8.Display books with fewer than 3 copies.
9.Display books that are unavailable.
10.Find the most available book.
11.Generate a restocking report.
12.Create a separate dictionary of books requiring immediate purchase.
Challenge
Generate a complete library summary report.
'''

# Library Dictionary
#------------------------------------------------------------

library = {
    "B101":{"title":"Python Basics","author":"ABC","copies":5},
    "B102":{"title":"Data Structures","author":"XYZ","copies":7},
    "B103":{"title":"Algorithms","author":"PQR","copies":2},
    "B104":{"title":"Machine Learning","author":"John","copies":4},
    "B105":{"title":"AI Fundamentals","author":"David","copies":1},
    "B106":{"title":"C Programming","author":"James","copies":8},
    "B107":{"title":"Java Programming","author":"Mark","copies":6},
    "B108":{"title":"DBMS","author":"Thomas","copies":3},
    "B109":{"title":"Computer Networks","author":"Kevin","copies":2},
    "B110":{"title":"Operating Systems","author":"Steve","copies":5},
    "B111":{"title":"Cloud Computing","author":"Robert","copies":4},
    "B112":{"title":"Cyber Security","author":"Chris","copies":2},
    "B113":{"title":"Big Data","author":"Daniel","copies":1},
    "B114":{"title":"Data Science","author":"Joseph","copies":6},
    "B115":{"title":"HTML","author":"Alex","copies":8},
    "B116":{"title":"CSS","author":"Ryan","copies":4},
    "B117":{"title":"JavaScript","author":"Jack","copies":5},
    "B118":{"title":"React JS","author":"Tom","copies":2},
    "B119":{"title":"Node JS","author":"Peter","copies":3},
    "B120":{"title":"Django","author":"Harry","copies":4},
    "B121":{"title":"Flask","author":"William","copies":2},
    "B122":{"title":"PHP","author":"Oliver","copies":7},
    "B123":{"title":"Linux","author":"Mason","copies":1},
    "B124":{"title":"Software Engineering","author":"Ethan","copies":5},
    "B125":{"title":"Compiler Design","author":"Logan","copies":2},
    "B126":{"title":"Discrete Mathematics","author":"Noah","copies":6},
    "B127":{"title":"Computer Graphics","author":"Lucas","copies":3},
    "B128":{"title":"Blockchain","author":"Henry","copies":1},
    "B129":{"title":"IoT","author":"Leo","copies":4},
    "B130":{"title":"Deep Learning","author":"Adam","copies":2}
}
while True:

    # Menu
    print("\n===== SMART LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book By ID")
    print("4. Search Book By Title")
    print("5. Update Copies")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. Display Books With Fewer Than 3 Copies")
    print("9. Display Unavailable Books")
    print("10. Most Available Book")
    print("11. Restocking Report")
    print("12. Immediate Purchase Report")
    print("13. Library Summary Report")
    print("14. Display All Books")
    print("15. Exit")

    choice = int(input("Enter Choice : "))

# 1. Add Book
#-------------------------------------------------------
    if choice == 1:

        book_id = input("Enter Book ID : ")

        if book_id in library:
            print("Book Already Exists")

        else:
            title = input("Enter Title : ")
            author = input("Enter Author : ")
            copies = int(input("Enter Copies : "))

            library[book_id] = {
                "title": title,
                "author": author,
                "copies": copies
            }

            print("Book Added Successfully")

# 2. Remove Book
#-------------------------------------------------------
    elif choice == 2:

        book_id = input("Enter Book ID : ")

        if book_id in library:
            del library[book_id]
            print("Book Removed Successfully")
        else:
            print("Book Not Found")

# 3. Search Book By ID
 #-------------------------------------------------------
    elif choice == 3:

        book_id = input("Enter Book ID : ")

        if book_id in library:

            print("Title :", library[book_id]["title"])
            print("Author :", library[book_id]["author"])
            print("Copies :", library[book_id]["copies"])

        else:
            print("Book Not Found")

 # 4. Search Book By Title
 #-------------------------------------------------------
    elif choice == 4:

        title = input("Enter Book Title : ")

        found = False

        for book_id in library:

            if library[book_id]["title"].lower() == title.lower():

                print(book_id,
                      library[book_id]["title"],
                      library[book_id]["author"],
                      library[book_id]["copies"])

                found = True

        if found == False:
            print("Book Not Found")

 # 5. Update Copies
 #-------------------------------------------------------
    elif choice == 5:

        book_id = input("Enter Book ID : ")

        if book_id in library:

            copies = int(input("Enter New Copies : "))
            library[book_id]["copies"] = copies

            print("Copies Updated Successfully")

        else:
            print("Book Not Found")

 # 6. Issue Book
 #-------------------------------------------------------
    elif choice == 6:

        book_id = input("Enter Book ID : ")

        if book_id in library:

            if library[book_id]["copies"] > 0:

                library[book_id]["copies"] -= 1

                print("Book Issued Successfully")

            else:
                print("Book Not Available")

        else:
            print("Book Not Found")

 # 7. Return Book
 #-------------------------------------------------------
    elif choice == 7:

        book_id = input("Enter Book ID : ")

        if book_id in library:

            library[book_id]["copies"] += 1

            print("Book Returned Successfully")

        else:
            print("Book Not Found")

# 8. Books With Less Than 3 Copies
#-------------------------------------------------------
    elif choice == 8:

        print("\nBooks With Less Than 3 Copies")

        for book_id in library:

            if library[book_id]["copies"] < 3:

                print(book_id,
                      library[book_id]["title"],
                      library[book_id]["copies"])

 # 9. Unavailable Books
#-------------------------------------------------------
    elif choice == 9:

        print("\nUnavailable Books")

        for book_id in library:

            if library[book_id]["copies"] == 0:

                print(book_id,
                      library[book_id]["title"])

# 10. Most Available Book
#-------------------------------------------------------
    elif choice == 10:

        max_copies = -1

        for book_id in library:

            if library[book_id]["copies"] > max_copies:

                max_copies = library[book_id]["copies"]
                best_book = book_id

        print("\nMost Available Book")

        print(best_book,
              library[best_book]["title"],
              max_copies)

# 11. Restocking Report
#-------------------------------------------------------
    elif choice == 11:

        print("\nRESTOCKING REPORT")

        for book_id in library:

            if library[book_id]["copies"] < 3:

                print(book_id,
                      library[book_id]["title"],
                      library[book_id]["copies"])

# 12. Immediate Purchase Dictionary
#-------------------------------------------------------
    elif choice == 12:

        purchase = {}

        for book_id in library:

            if library[book_id]["copies"] <= 1:

                purchase[book_id] = library[book_id]

        print("\nBooks Requiring Immediate Purchase")

        for book_id in purchase:

            print(book_id,
                  purchase[book_id]["title"],
                  purchase[book_id]["copies"])

# 13. Library Summary Report
#-------------------------------------------------------
    elif choice == 13:

        total_books = len(library)
        total_copies = 0

        max_copies = -1

        for book_id in library:

            total_copies += library[book_id]["copies"]

            if library[book_id]["copies"] > max_copies:

                max_copies = library[book_id]["copies"]
                best_book = book_id

        print("\n===== LIBRARY SUMMARY REPORT =====")

        print("Total Books :", total_books)
        print("Total Copies :", total_copies)

        print("\nMost Available Book")

        print(best_book,
              library[best_book]["title"],
              max_copies)

    # 14. Display All Books
    elif choice == 14:

        print("\nLibrary Records")

        for book_id in library:

            print(book_id,
                  library[book_id]["title"],
                  library[book_id]["author"],
                  library[book_id]["copies"])

    # 15. Exit
    elif choice == 15:

        print("Program Ended Successfully")
        break

    else:

        print("Invalid Choice")