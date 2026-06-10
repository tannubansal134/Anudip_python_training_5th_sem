'''Program to read data line by line from a file.'''
# Open the file in read mode
filev = open('sentences.txt', 'r')
#to check file is open or not
if not filev:
    exit("Error opening the file.")
# Read first line from the file
line = filev.readline()
# Loop until the end of the file is reached
while line:
    # Print the line read from the file
    print(line, end='')  # end='' to avoid adding extra newline
    # Read the next line from the file
    line = filev.readline()
# Close the file
filev.close()
#----------------------------------------------------------------------------