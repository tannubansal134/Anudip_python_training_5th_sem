'''Problem Statement
A company wants to maintain backups of important documents. Create a program to copy the contents of one file into another.
Sample Input/Data
Source File (notes.txt)
Python supports file handling. 
Functions improve code reusability. 
Dictionaries store data in key-value pairs.
Tasks
1.Read the contents of the source file.
2.Copy the entire content to another file named backup.txt.
3.Display a success message.
4.Verify whether both files contain the same number of lines.
'''

# Open source file in read mode
#-------------------------------------------------
source = open("notes.txt", "r")

# Read complete content from source file
#-------------------------------------------------
content = source.read()
source.close()

# Open backup file in write mode
#-------------------------------------------------
backup = open("backup.txt", "w")

# Write content into backup file
#-------------------------------------------------
backup.write(content)
backup.close()

# Reopen files to count lines
#-------------------------------------------------
source = open("notes.txt", "r")
backup = open("backup.txt", "r")

# Read all lines
#-------------------------------------------------
source_lines = source.readlines()
backup_lines = backup.readlines()

# Count lines
#-------------------------------------------------
source_count = len(source_lines)
backup_count = len(backup_lines)

# Display results
#-------------------------------------------------
print("File copied successfully.")
print("Source File Lines:", source_count)
print("Backup File Lines:", backup_count)

# Verify line counts
#-------------------------------------------------
if source_count == backup_count:
    print("Verification Status: successful")
else:
    print("Verification Status: failed")
source.close()
backup.close()