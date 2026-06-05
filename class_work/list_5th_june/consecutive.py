# List of numbers
numbers = [4, 5, 6, 10, 11, 15, 16, 17]

# List to store consecutive pairs
consecutive_pairs = []

# Loop through the list
for i in range(len(numbers) - 1):

    # Check if the next number is consecutive
    if numbers[i + 1] == numbers[i] + 1:

        # Display the consecutive pair
        print(numbers[i], "and", numbers[i + 1], "are consecutive")

        # Store the pair in a new list
        consecutive_pairs.append((numbers[i], numbers[i + 1]))

# Display all consecutive pairs
print("\nList of consecutive pairs:")
print(consecutive_pairs)