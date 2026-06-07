"""
Program: Inventory Management System

This program performs the following tasks:
1. Displays products with stock less than 10.
2. Counts products having stock more than 50.
3. Finds the product with the minimum stock.
4. Creates a list of products that require restocking (stock < 20).
5. Calculates the total inventory count.
"""

# Dictionary containing product names and stock quantities
inventory = {
    "Notebook": 45,
    "Pen": 120,
    "Pencil": 80,
    "Eraser": 25,
    "Marker": 15,
    "Stapler": 8,
    "Glue": 12,
    "Scale": 30,
    "Folder": 5,
    "Calculator": 3
}

#----------------------------------------------
#Display products with stock less than 10

print("Products with stock less than 10:")
for product, stock in inventory.items():
    if stock < 10:
        print(product, ":", stock)

#---------------------------------------------
# Count products having stock more than 50

count = 0
for stock in inventory.values():
    if stock > 50:
        count += 1

print("\nProducts having stock more than 50:", count)

#-------------------------------------
# Find the product with minimum stock

min_product = min(inventory, key=inventory.get)

print("\nProduct with minimum stock:")
print(min_product, ":", inventory[min_product])

#----------------------------------------------
# Create a list of products requiring restocking
# (stock less than 20)

restock = []

for product, stock in inventory.items():
    if stock < 20:
        restock.append(product)

print("\nProducts requiring restocking:")
print(restock)

#-------------------------------------
# Calculate total inventory count

total_stock = sum(inventory.values())

print("\nTotal Inventory Count:", total_stock)