"""
Program: E-Commerce Order Analysis

This program performs the following tasks:
1. Display all products costing more than ₹1000.
2. Find the most expensive product.
3. Calculate the total order value.
4. Count products costing below ₹1000.
"""

orders = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Pen Drive", 600)
]

# --------------------------------------------------
# Task 1: Display all products costing more than ₹1000

print("Products Costing More Than ₹1000")

for product in orders:
    if product[1] > 1000:
        print("Product Name :", product[0])
        print("Price : ₹", product[1])

# --------------------------------------------------
# Task 2: Find the most expensive product

most_expensive = orders[0]

for product in orders:
    if product[1] > most_expensive[1]:
        most_expensive = product

print("\nMost Expensive Product")
print("Product Name :", most_expensive[0])
print("Price : ₹", most_expensive[1])

# --------------------------------------------------
# Task 3: Calculate the total order value

total_value = 0

for product in orders:
    total_value += product[1]

print("\nTotal Order Value : ₹", total_value)

# --------------------------------------------------
# Task 4: Count products costing below ₹1000

count = 0

for product in orders:
    if product[1] < 1000:
        count += 1

print("\nNumber of Products Costing Below ₹1000 :", count)