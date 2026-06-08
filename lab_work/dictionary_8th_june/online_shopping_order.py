"""
Program: Online Shopping Order Analytics

This program performs the following tasks:
1. Display products sold more than 20 times.
2. Find the best-selling product.
3. Find the least-selling product.
4. Calculate total products sold.
5. Create a list of products requiring promotion (sales < 15).
6. Count products having sales between 10 and 30.
"""

# Dictionary containing product sales data
sales = {
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

#--------------------------------------------------
# Display products sold more than 20 times

print("Products Sold More Than 20 Times:")
for product, quantity in sales.items():
    if quantity > 20:
        print(product, end=" ")
print()

#--------------------------------------------------
# Find the best-selling product

best_product = max(sales, key=sales.get)
print("\nBest Selling Product:", best_product, f"({sales[best_product]})")

#--------------------------------------------------
# Find the least-selling product

least_product = min(sales, key=sales.get)
print("Least Selling Product:", least_product, f"({sales[least_product]})")

#--------------------------------------------------
# Calculate total products sold

total_sold = sum(sales.values())
print("Total Units Sold:", total_sold)

#--------------------------------------------------
# Create a list of products requiring promotion
# product with sales less than 15

promotion_products = []

for product, quantity in sales.items():
    if quantity < 15:
        promotion_products.append(product)

print("Products Requiring Promotion:", promotion_products)

#--------------------------------------------------
# Count products having sales between 10 and 30
# (Including 10 and 30)

count = 0

for quantity in sales.values():
    if 10 <= quantity <= 30:
        count += 1

print("Products Having Sales Between 10 and 30:", count)