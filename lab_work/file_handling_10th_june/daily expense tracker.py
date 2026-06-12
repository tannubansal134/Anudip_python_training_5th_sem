''' Problem Statement
Daily expenses are recorded in expenses.txt.
File Format
Food,450
Travel,300
Shopping,1200
Electricity,850
Internet,700
Entertainment,600
Medicine,400
Education,1500
Fuel,900
Miscellaneous,250
Requirements
Develop a program to:
1. Display all expenses. 
2. Calculate total expenditure. 
3. Find the category with highest and lowest spending. 
4. Display expenses greater than ₹800. 
5. Add a new expense category. 
6. Update an existing expense amount. 
7. Generate a summary report in report.txt containing: 
o Total Expenses 
o Highest Expense Category 
o Lowest Expense Category 
o Categories spending more than ₹800'''


# --------------------------------------------
# Function to read expenses from file
# --------------------------------------------
def read_expenses():
    expenses = {}

    file = open("expenses.txt", "r")

    for line in file:
        data = line.strip().split(",")
        category = data[0]
        amount = int(data[1])
        expenses[category] = amount

    file.close()
    return expenses


# --------------------------------------------
# Function to display all expenses
# --------------------------------------------
def display_expenses(expenses):
    print("\n----- All Expenses -----")

    for category, amount in expenses.items():
        print(category, ":", amount)


# --------------------------------------------
# Function to calculate total expenditure
# --------------------------------------------
def total_expenses(expenses):
    total = sum(expenses.values())
    print("\nTotal Expenditure = ₹", total)
    return total


# --------------------------------------------
# Function to find highest and lowest expense
# --------------------------------------------
def highest_lowest(expenses):

    highest_category = max(expenses, key=expenses.get)
    lowest_category = min(expenses, key=expenses.get)

    print("\nHighest Expense:")
    print(highest_category, "=", expenses[highest_category])

    print("\nLowest Expense:")
    print(lowest_category, "=", expenses[lowest_category])

    return highest_category, lowest_category


# --------------------------------------------
# Function to display expenses greater than 800
# --------------------------------------------
def greater_than_800(expenses):

    print("\nExpenses Greater Than ₹800")

    for category, amount in expenses.items():
        if amount > 800:
            print(category, ":", amount)


# --------------------------------------------
# Function to add new expense category
# --------------------------------------------
def add_expense(expenses):

    category = input("\nEnter New Category: ")
    amount = int(input("Enter Amount: "))

    expenses[category] = amount

    file = open("expenses.txt.", "w")

    for c, a in expenses.items():
        file.write(c + "," + str(a) + "\n")

    file.close()

    print("New Expense Added Successfully.")


# --------------------------------------------
# Function to update existing expense
# --------------------------------------------
def update_expense(expenses):

    category = input("\nEnter Category to Update: ")

    if category in expenses:
        amount = int(input("Enter New Amount: "))
        expenses[category] = amount

        file = open("expenses.txt.", "w")

        for c, a in expenses.items():
            file.write(c + "," + str(a) + "\n")

        file.close()

        print("Expense Updated Successfully.")

    else:
        print("Category Not Found.")


# --------------------------------------------
# Function to generate report.txt
# --------------------------------------------
def generate_report(expenses):

    total = sum(expenses.values())
    highest = max(expenses, key=expenses.get)
    lowest = min(expenses, key=expenses.get)

    report = open("report.txt", "w")

    report.write("===== Expense Summary Report =====\n\n")

    report.write("Total Expenses : ₹" + str(total) + "\n")
    report.write("Highest Expense Category : " + highest + "\n")
    report.write("Lowest Expense Category : " + lowest + "\n\n")

    report.write("Categories Spending More Than ₹800\n")

    for category, amount in expenses.items():
        if amount > 800:
            report.write(category + " : ₹" + str(amount) + "\n")

    report.close()

    print("\nReport Generated Successfully (report.txt)")


# ============================================
# Main Program
# ============================================

expenses = read_expenses()

display_expenses(expenses)

total_expenses(expenses)

highest_lowest(expenses)

greater_than_800(expenses)

add_expense(expenses)

expenses = read_expenses()

update_expense(expenses)

expenses = read_expenses()

generate_report(expenses)