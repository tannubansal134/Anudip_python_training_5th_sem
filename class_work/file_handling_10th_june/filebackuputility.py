# ==========================================================
# File Backup Utility
# ==========================================================
'''Problem:
 Create an exact copy of a source file into a
 destination file.

 Steps:
 1. Take source file name from user
 2. Take destination file name from user
 3. Read source file contents
 4. Write contents into destination file
 5. Display success message'''

# ==========================================================
# File Backup Utility
# ==========================================================
'''Problem:
 Create an exact copy of a source file into a
 destination file.

 Steps:
 1. Take source file name from user
 2. Take destination file name from user
 3. Read source file contents
 4. Write contents into destination file
 5. Display success message'''
# ==========================================================


# ----------------------------------------------------------
# Accept file names from user
# ----------------------------------------------------------
source_file = input("Enter Source File Name      : ")
destination_file = input("Enter Destination File Name : ")


# ----------------------------------------------------------
# Open source file in read mode
# Read complete contents
# ----------------------------------------------------------
source = open(source_file, "r")

data = source.read()

source.close()


# ----------------------------------------------------------
# Open destination file in write mode
# Write source file contents into destination file
# ----------------------------------------------------------
destination = open(destination_file, "w")

destination.write(data)

destination.close()


# ----------------------------------------------------------
# Display Success Message
# ----------------------------------------------------------
print("\nFile copied successfully.")

print(
    f"All contents from '{source_file}' "
    f"have been copied to '{destination_file}'."
)