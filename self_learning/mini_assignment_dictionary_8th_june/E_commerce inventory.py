"""
        ONLINE STORE MANAGEMENT SYSTEM

This program performs the following tasks:

1. Display all products
2. Add a new product
3. Update stock after sales
4. Find out-of-stock products
5. Find products with stock less than 5
6. Calculate total inventory value
7. Find best-selling product
8. Find least-selling product
9. Calculate total revenue generated
10. Generate low-stock report
11. Display products whose sales exceed average sales
12. Create a dictionary of product eligible for promotion (sales < 10)
13. Generate complete business report
"""
# --------------------------------------------------
# Product Dictionary (30 Products)

products = {
    "P101": {"name": "Laptop", "price": 55000, "stock": 12, "sold": 25},
    "P102": {"name": "Mouse", "price": 500, "stock": 20, "sold": 40},
    "P103": {"name": "Keyboard", "price": 1200, "stock": 8, "sold": 18},
    "P104": {"name": "Monitor", "price": 9000, "stock": 6, "sold": 15},
    "P105": {"name": "Printer", "price": 7000, "stock": 0, "sold": 12},
    "P106": {"name": "Speaker", "price": 1500, "stock": 3, "sold": 9},
    "P107": {"name": "Headphone", "price": 2500, "stock": 15, "sold": 30},
    "P108": {"name": "Webcam", "price": 1800, "stock": 4, "sold": 7},
    "P109": {"name": "Hard Disk", "price": 4500, "stock": 10, "sold": 22},
    "P110": {"name": "Pendrive", "price": 700, "stock": 25, "sold": 50},
    "P111": {"name": "Tablet", "price": 18000, "stock": 7, "sold": 11},
    "P112": {"name": "Smart Watch", "price": 5000, "stock": 2, "sold": 8},
    "P113": {"name": "Mobile", "price": 22000, "stock": 9, "sold": 35},
    "P114": {"name": "Power Bank", "price": 1500, "stock": 14, "sold": 28},
    "P115": {"name": "Router", "price": 3000, "stock": 1, "sold": 5},
    "P116": {"name": "Projector", "price": 25000, "stock": 5, "sold": 6},
    "P117": {"name": "Scanner", "price": 6000, "stock": 0, "sold": 4},
    "P118": {"name": "Microphone", "price": 2200, "stock": 11, "sold": 13},
    "P119": {"name": "Camera", "price": 35000, "stock": 3, "sold": 10},
    "P120": {"name": "Tripod", "price": 1200, "stock": 16, "sold": 17},
    "P121": {"name": "SSD", "price": 5000, "stock": 8, "sold": 21},
    "P122": {"name": "RAM", "price": 3200, "stock": 5, "sold": 16},
    "P123": {"name": "Graphics Card", "price": 45000, "stock": 2, "sold": 9},
    "P124": {"name": "CPU", "price": 28000, "stock": 4, "sold": 14},
    "P125": {"name": "Motherboard", "price": 12000, "stock": 6, "sold": 12},
    "P126": {"name": "Charger", "price": 800, "stock": 30, "sold": 45},
    "P127": {"name": "Cable", "price": 300, "stock": 40, "sold": 55},
    "P128": {"name": "UPS", "price": 6500, "stock": 3, "sold": 8},
    "P129": {"name": "VR Headset", "price": 18000, "stock": 1, "sold": 3},
    "P130": {"name": "Gaming Chair", "price": 12000, "stock": 2, "sold": 7}
}

# --------------------------------------------------
# Display All Products

def display_products():

    print("\n----- PRODUCT RECORDS -----")

    for pid, details in products.items():
        print(pid, ":", details)

# --------------------------------------------------
# Add New Product

def add_product():

    pid = input("Enter Product ID: ")

    if pid in products:
        print("Product Already Exists")

    else:
        name = input("Enter Product Name: ")
        price = float(input("Enter Price: "))
        stock = int(input("Enter Stock: "))
        sold = int(input("Enter Sold Quantity: "))

        products[pid] = {
            "name": name,
            "price": price,
            "stock": stock,
            "sold": sold
        }

        print("Product Added Successfully")

# --------------------------------------------------
# Update Stock After Sales

def update_stock():

    pid = input("Enter Product ID: ")

    if pid in products:

        qty = int(input("Enter Quantity Sold: "))

        if qty <= products[pid]["stock"]:

            products[pid]["stock"] -= qty
            products[pid]["sold"] += qty

            print("Stock Updated Successfully")

        else:
            print("Insufficient Stock")

    else:
        print("Product Not Found")

# --------------------------------------------------
# Find Out Of Stock Products

def out_of_stock():

    print("\nOut Of Stock Products")

    for pid, details in products.items():

        if details["stock"] == 0:
            print(pid, details)

# --------------------------------------------------
# Find Products With Stock Less Than 5

def low_stock_products():

    print("\nProducts With Stock Less Than 5")

    for pid, details in products.items():

        if details["stock"] < 5:
            print(pid, details)

# --------------------------------------------------
# Calculate Total Inventory Value

def inventory_value():

    total = 0

    for details in products.values():
        total += details["price"] * details["stock"]

    print("Total Inventory Value =", total)

    return total

# --------------------------------------------------
# find Best Selling Product

def best_selling():

    best = max(products, key=lambda x: products[x]["sold"])

    print("\nBest Selling Product")
    print(best, products[best])

# --------------------------------------------------
# find Least Selling Product

def least_selling():

    least = min(products, key=lambda x: products[x]["sold"])

    print("\nLeast Selling Product")
    print(least, products[least])

# --------------------------------------------------
# calculate Total Revenue Generated
# --------------------------------------------------
def total_revenue():

    revenue = 0

    for details in products.values():
        revenue += details["price"] * details["sold"]

    print("Total Revenue =", revenue)

    return revenue

# --------------------------------------------------
# Generate Low Stock Report

def low_stock_report():

    print("\n----- LOW STOCK REPORT -----")

    for pid, details in products.items():

        if details["stock"] < 5:
            print(pid, details["name"], "Stock =", details["stock"])

# --------------------------------------------------
# Products Above Average Sales

def above_average_sales():

    total_sales = 0

    for details in products.values():
        total_sales += details["sold"]

    avg_sales = total_sales / len(products)

    print("\nAverage Sales =", round(avg_sales, 2))
    print("Products Above Average Sales")

    for pid, details in products.items():

        if details["sold"] > avg_sales:
            print(pid, details)

# --------------------------------------------------
# Promotion Products Dictionary Sales < 10

def promotion_products():

    promotion = {}

    for pid, details in products.items():

        if details["sold"] < 10:
            promotion[pid] = details

    print("\nPromotion Products Dictionary")

    for pid, details in promotion.items():
        print(pid, details)

# --------------------------------------------------
# Complete Business Report

def business_report():

    print("\n")
    print("========== BUSINESS REPORT ==========")

    inventory = inventory_value()
    revenue = total_revenue()

    best = max(products, key=lambda x: products[x]["sold"])
    least = min(products, key=lambda x: products[x]["sold"])

    print("\nTotal Products :", len(products))
    print("Inventory Value :", inventory)
    print("Revenue Generated :", revenue)

    print("\nBest Selling Product")
    print(best, products[best])

    print("\nLeast Selling Product")
    print(least, products[least])

    low_stock = 0

    for details in products.values():

        if details["stock"] < 5:
            low_stock += 1

    print("\nLow Stock Products :", low_stock)

    print("===================================")

# --------------------------------------------------
# Main Menu

while True:

    print("\n")
    print("===== ONLINE STORE MANAGEMENT =====")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock After Sales")
    print("4. Out Of Stock Products")
    print("5. Products With Stock Less Than 5")
    print("6. Total Inventory Value")
    print("7. Best Selling Product")
    print("8. Least Selling Product")
    print("9. Total Revenue")
    print("10. Low Stock Report")
    print("11. Products Above Average Sales")
    print("12. Promotion Products")
    print("13. Complete Business Report")
    print("14. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_products()

    elif choice == 2:
        add_product()

    elif choice == 3:
        update_stock()

    elif choice == 4:
        out_of_stock()

    elif choice == 5:
        low_stock_products()

    elif choice == 6:
        inventory_value()

    elif choice == 7:
        best_selling()

    elif choice == 8:
        least_selling()

    elif choice == 9:
        total_revenue()

    elif choice == 10:
        low_stock_report()

    elif choice == 11:
        above_average_sales()

    elif choice == 12:
        promotion_products()

    elif choice == 13:
        business_report()

    elif choice == 14:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")