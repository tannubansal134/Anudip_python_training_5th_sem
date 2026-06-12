'''Problem Statement 
The number of available copies of books in a library is stored below. Sample Data books = {     "Python": 5, 
    "Java": 2, 
    "DBMS": 4, 
    "Networking": 1, 
    "OS": 3, 
    "AI": 6, 
    "ML": 2, 
    "Cloud": 5, 
    "Cyber Security": 1, 
    "Web Development": 4 
} 
Tasks 
1.	Display books with fewer than 3 copies.  
2.	Find the book with maximum copies.  
3.	Find the book with minimum copies.  
4.	Count total books available.  
5.	Generate a restocking list.  
'''
# ==========================================================
# Library Book Availability System
# ==========================================================

books = {
    "Python": 5,
    "Java": 2,
    "DBMS": 4,
    "Networking": 1,
    "OS": 3,
    "AI": 6,
    "ML": 2,
    "Cloud": 5,
    "Cyber Security": 1,
    "Web Development": 4
}

# 1. Display books with fewer than 3 copies
#-------------------------------------------------------------
print("Books Requiring Attention:")

for book in books:
    if books[book] < 3:
        print(book)

# 2. Find the book with maximum copies
#-------------------------------------------------------------
max_book = ""
max_copies = 0

for book in books:
    if books[book] > max_copies:
        max_copies = books[book]
        max_book = book

print("\nBook with Maximum Copies:")
print(max_book, "(", max_copies, "copies )")

# 3. Find the book with minimum copies
#-----------------------------------------------------------------
min_book = ""
min_copies = 999

for book in books:
    if books[book] < min_copies:
        min_copies = books[book]
        min_book = book

print("\nBook with Minimum Copies:")
print(min_book, "(", min_copies, "copies )")

# 4. Count total books available
#-------------------------------------------------------------
total_copies = 0

for book in books:
    total_copies = total_copies + books[book]

print("\nTotal Copies Available:", total_copies)

# 5. Generate a restocking list
#--------------------------------------------------------------
restocking_list = []

for book in books:
    if books[book] < 3:
        restocking_list.append(book)

print("\nRestocking List:")
print(restocking_list)
'''Sample Output 
Books Requiring Attention: 
Java 
Networking 
ML 
Cyber Security 
 
Book with Maximum Copies: 
AI (6 copies) 
 
Book with Minimum Copies: 
Networking (1 copy) 
 
Total Copies Available: 33 
 
Restocking List: 
['Java', 'Networking', 'ML', 'Cyber Security'] 
'''