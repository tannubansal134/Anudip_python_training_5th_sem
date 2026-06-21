# Write a program to read a text file and count the total number of words, lines, and characters present in the file.

try:
    # Input file name from the user
    #----------------------------------------------------
    file_name = input("Enter the file name: ")

    # Open the file in read mode
    with open(file_name, "r") as file:
        content = file.read()      
        file.seek(0)               
        lines = file.readlines()   

    line_count = len(lines)
    word_count = len(content.split())

    char_count = len(content)

# Display the results
#----------------------------------------------------------------

    print("\nFile Analysis")
    print("-------------")
    print("Total Lines      :", line_count)
    print("Total Words      :", word_count)
    print("Total Characters :", char_count)

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An error occurred:", e)