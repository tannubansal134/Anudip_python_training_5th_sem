"""
Program: Mobile Contact Directory

This program performs the following tasks:
1. Displays all contact names in alphabetical order.
2. Counts the total number of contacts.
3. Searches for a given contact name.
4. Creates a list of contacts whose names start with a vowel.
5. Stops the search using break once the contact is found.
"""

# Dictionary containing contact names and phone numbers
contacts = {
    "Amit": "9876543210",
    "Priya": "9876543211",
    "Rohan": "9876543212",
    "Neha": "9876543213",
    "Anjali": "9876543214",
    "Karan": "9876543215",
    "Pooja": "9876543216",
    "Arjun": "9876543217",
    "Sneha": "9876543218",
    "Rahul": "9876543219"
}

#-------------------------------------------------------
# Display all contact names in alphabetical order

print("Contact Names in Alphabetical Order:")

for name in sorted(contacts.keys()):
    print(name)

#-----------------------------------------
# Count the total number of contacts

total_contacts = len(contacts)

print("\nTotal Number of Contacts:", total_contacts)

#-----------------------------------------
# Search for a given contact name
# and stop using break when found

search_name = input("\nEnter contact name to search: ")

found = False

for name, number in contacts.items():

    if name.lower() == search_name.lower():
        print("Contact Found")
        print("Name :", name)
        print("Phone Number :", number)
        found = True
        break

if not found:
    print("Contact not found.")

#----------------------------------------------
# Create a list of contacts whose names
# start with a vowel

vowel_contacts = []

for name in contacts.keys():

    if name[0].upper() in ['A', 'E', 'I', 'O', 'U']:
        vowel_contacts.append(name)

print("\nContacts whose names start with a vowel:")
print(vowel_contacts)