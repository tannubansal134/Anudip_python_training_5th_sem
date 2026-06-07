"""
Program: Product Price Analysis

This program performs the following tasks:
1. Displays products costing more than ₹5000.
2. Counts products costing less than ₹3000.
3. Finds the most expensive product.
4. Creates a list of products priced between ₹2000 and ₹10000.
5. Calculates the total value of all products.
"""

# Dictionary containing product names and prices
prices = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1800,
    "Monitor": 12000,
    "Printer": 9000,
    "Tablet": 28000,
    "Speaker": 3500,
    "Webcam": 2500,
    "Headphones": 4200,
    "Router": 3200
}

#-------------------------------------------------
# Display products costing more than ₹5000

print("Products costing more than ₹5000:")

for product, price in prices.items():
    if price > 5000:
        print(product, ":", price)

#-----------------------------------------------
# count products costing less than ₹3000

count = 0

for price in prices.values():
    if price < 3000:
        count += 1

print("\nNumber of products costing less than ₹3000:", count)

#-------------------------------------------
# Find the most expensive product

expensive_product = max(prices, key=prices.get)

print("\nMost Expensive Product:")
print(expensive_product, ":", prices[expensive_product])

#-----------------------------------------
# Create a list of products priced
# between ₹2000 and ₹10000

product_list = []

for product, price in prices.items():
    if 2000 <= price <= 10000:
        product_list.append(product)

print("\nProducts priced between ₹2000 and ₹10000:")
print(product_list)

#--------------------------------------------------
# Calculate the total value of all products

total_value = sum(prices.values())

print("\nTotal Value of All Products: ₹", total_value)