# Initialize counters and total amount
above_50000 = 0
below_1000 = 0
total_amount = 0

# Read transaction amounts continuously
while True:
    amount = float(input("Enter transaction amount (-1 to stop): "))

    # Stop when -1 is entered
    if amount == -1:
        break

    # Add to total transaction amount
    total_amount += amount

    # Count transactions above ₹50,000
    if amount > 50000:
        above_50000 += 1

    # Count transactions below ₹1,000
    if amount < 1000:
        below_1000 += 1

# Display results
print("\nTransaction Summary")
print("Transactions above ₹50,000:", above_50000)
print("Transactions below ₹1,000:", below_1000)
print("Total transaction amount: ₹", total_amount)