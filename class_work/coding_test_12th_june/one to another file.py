# Create a program to copy the contents of one file into another file and display the total number of lines copied.

# Input source and destination file names
#-----------------------------------------------------------------
source_file = input("Enter source file name: ")
destination_file = input("Enter destination file name: ")

try:
    # Open the source file in read mode
    #------------------------------------------------
    with open(source_file, "r") as file1:
        data = file1.readlines()   

    # Open the destination file in write mode
    #-----------------------------------------------------------------------------
    with open(destination_file, "w") as file2:
        file2.writelines(data)     

    # Count the total number of lines copied
    #---------------------------------------------------
    line_count = len(data)

    # Display result
    #------------------------------------------------------
    print("File copied successfully.")
    print("Total number of lines copied:", line_count)

except FileNotFoundError:
    print("Error: Source file not found.")

except Exception as e:
    print("An error occurred:", e)