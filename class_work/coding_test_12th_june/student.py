# Write a program to store student names in a tuple and search for a given name using selection statements. Display an appropriate message if the name is not found.
# Tuple containing student names
#-------------------------------------------------------------
students = ("Anuj", "Rahul", "Priya", "Neha", "Amit", "Sneha")

# Take the name to search from the user
#------------------------------------------------------------
search_name = input("Enter the student name to search: ")

# Use selection statement to check if the name exists in the tuple
#--------------------------------------------------------------------
if search_name in students:
    print(search_name, "is found in the student list.")
else:
    print(search_name, "is not found in the student list.")