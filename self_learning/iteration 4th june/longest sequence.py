# Read the number of values to be entered
N = int(input("Enter N: "))

# Read the first number
prev = int(input())

# Length of current increasing sequence
current_len = 1

# Length of longest increasing sequence
max_len = 1

# Read remaining N-1 numbers one by one
for i in range(N - 1):
    num = int(input())

    # Check if the sequence is increasing
    if num > prev:
        current_len += 1
    else:
        current_len = 1

    # Update maximum length if needed
    if current_len > max_len:
        max_len = current_len

    # Store current number as previous for next comparison
    prev = num

# Display the result
print("Longest Sequence Length =", max_len)