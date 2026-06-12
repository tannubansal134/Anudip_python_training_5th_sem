'''Problem Statement
Contacts are stored in contacts.txt.
File Format
Anuj,9876543210 
Rahul,9876543211
Priya,9876543212
Neha,9876543213
Amit,9876543214
Sneha,9876543215 
Karan,9876543216 
Pooja,9876543217 
Rohit,9876543218 
Anjali,9876543219
Requirements
Create a menu-driven application to:
1. Display all contacts.
2. Search a contact by name.
3. Add a new contact.
4. Update an existing contact number.
5. Delete a contact.
6. Display contacts whose names start with a vowel.
7. Save all modifications back to the file.
'''
#---------------------------------------------------
# Function to load contacts from file
#---------------------------------------------------
def load_contacts():

    contacts = {}
    file = open("contacts.txt", "r")
    lines = file.readlines()
    for line in lines:

        data = line.strip().split(",")

        name = data[0]
        number = data[1]

        contacts[name] = number
    file.close()

    return contacts

#---------------------------------------------------
# Function to save contacts back to file
#---------------------------------------------------
def save_contacts(contacts):
    file = open("contacts.txt", "w")

    for name in contacts:
        file.write(f"{name},{contacts[name]}\n")
    file.close()

#---------------------------------------------------
# Function to display all contacts
#---------------------------------------------------
def display_contacts(contacts):

    print("\n----- ALL CONTACTS -----")

    print("Name\t\tPhone Number")

    for name in contacts:
        print(name, "\t", contacts[name])

#---------------------------------------------------
# Function to search contact by name
#---------------------------------------------------
def search_contact(contacts):

    name = input("Enter Contact Name : ")

    if name in contacts:

        print("\nContact Found")
        print("Name   :", name)
        print("Number :", contacts[name])

    else:
        print("Contact not found.")

#---------------------------------------------------
# Function to add new contact
#---------------------------------------------------
def add_contact(contacts):

    name = input("Enter Name : ")
    number = input("Enter Mobile Number : ")

    if name not in contacts:
        contacts[name] = number
        save_contacts(contacts)

        print("Contact Added Successfully.")

    else:
        print("Contact already exists.")

#---------------------------------------------------
# Function to update contact number
#---------------------------------------------------
def update_contact(contacts):

    name = input("Enter Contact Name : ")

    if name in contacts:

        new_number = input("Enter New Mobile Number : ")
        contacts[name] = new_number
        save_contacts(contacts)

        print("Contact Updated Successfully.")

    else:
        print("Contact not found.")

#---------------------------------------------------
# Function to delete contact
#---------------------------------------------------
def delete_contact(contacts):

    name = input("Enter Contact Name : ")

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)

        print("Contact Deleted Successfully.")

    else:
        print("Contact not found.")

#---------------------------------------------------
# Function to display contacts starting with vowels
#---------------------------------------------------
def vowel_contacts(contacts):

    print("\n----- CONTACTS STARTING WITH VOWELS -----")

    vowels = "AEIOUaeiou"

    found = False

    for name in contacts:

        if name[0] in vowels:

            print(name, "-", contacts[name])

            found = True

    if found == False:
        print("No contact starts with a vowel.")


# -----------------------------------------
# Main Program
# -----------------------------------------

while True:
    contacts = load_contacts()

    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Display All Contacts")
    print("2. Search Contact")
    print("3. Add New Contact")
    print("4. Update Contact Number")
    print("5. Delete Contact")
    print("6. Display Contacts Starting With Vowels")
    print("7. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        display_contacts(contacts)

    elif choice == "2":
        search_contact(contacts)

    elif choice == "3":
        add_contact(contacts)

    elif choice == "4":
        update_contact(contacts)

    elif choice == "5":
        delete_contact(contacts)

    elif choice == "6":
        vowel_contacts(contacts)

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")