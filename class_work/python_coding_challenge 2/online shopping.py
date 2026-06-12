'''Problem Statement 
An online store maintains stock quantities of products. Sample Data 
inventory = {     "Laptop": 15, 
    "Mouse": 45, 
    "Keyboard": 32, 
    "Monitor": 12, 
    "Headphones": 28, 
    "Printer": 8, 
    "Webcam": 20, 
    "Speaker": 18, 
    "Tablet": 10, 
    "Router": 25 
} 
Tasks 
1.	Display products with stock below 15 units.  
2.	Find the product with maximum stock.  
3.	Find the product with minimum stock.  
4.	Calculate total stock available.  
5.	Create a list of products requiring restocking (<10 units).  
'''
# ==========================================================
# Online Store Inventory Management System
# ==========================================================

inventory = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

# 1. Products with stock below 15
print("Products with Stock Below 15:")

for product in inventory:
    if inventory[product] < 15:
        print(product)

# 2. Product with maximum stock
highest_product = ""
highest_stock = 0

for product in inventory:
    if inventory[product] > highest_stock:
        highest_stock = inventory[product]
        highest_product = product

print("\nHighest Stock Product:")
print(highest_product, "(", highest_stock, "units )")

# 3. Product with minimum stock
lowest_product = ""
lowest_stock = 999

for product in inventory:
    if inventory[product] < lowest_stock:
        lowest_stock = inventory[product]
        lowest_product = product

print("\nLowest Stock Product:")
print(lowest_product, "(", lowest_stock, "units )")

# 4. Total stock available
total_stock = 0

for product in inventory:
    total_stock = total_stock + inventory[product]

print("\nTotal Stock Available:", total_stock)

# 5. Products requiring restocking
restocking_products = []

for product in inventory:
    if inventory[product] < 10:
        restocking_products.append(product)

print("\nProducts Requiring Restocking:")
print(restocking_products)

'''Sample Output 
Products with Stock Below 15: 
Monitor 
Printer 
Tablet 
 
Highest Stock Product: 
Mouse (45 units) 
 
Lowest Stock Product: 
Printer (8 units) 
 
Total Stock Available: 213 
 
Products Requiring Restocking: 
['Printer'] 
'''