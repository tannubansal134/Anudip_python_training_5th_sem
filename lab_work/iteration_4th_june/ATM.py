# Program for simple banking system using menu-driven approach 

# Initial balance
balance = 10000

while True:
    # Display menu
    print("\n--- Banking Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # Check balance
    if choice == 1:
        print("Your current balance is:", balance)

    # Deposit money
    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print("Amount deposited successfully!")
        print("Updated balance:", balance)

    # Withdraw money
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))

        # Check if sufficient balance is available
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful!")
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance! Withdrawal denied.")

    # Exit program
    elif choice == 4:
        print("Thank you for using the banking system.")
        break

    else:
        print("Invalid choice! Please try again.")