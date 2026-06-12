'''Problem Statement
An online store wants to manage products and sales.
Example Structure
products = { 
"P101": {
 "name": "Laptop", 
 "price": 55000, 
 "stock": 12, 
 "sold": 25 } 
 }
Maintain records of at least 30 products.
Requirements
1.Display all products.
2.Add a new product.
3.Update stock after sales.
4.Find out-of-stock products.
5.Find products with stock less than 5.
6.Calculate total inventory value.
7.Find best-selling product.
8.Find least-selling product.
9.Calculate total revenue generated.
10.Generate a low-stock report.
11.Display products whose sales exceed the average sales.
12.Create a dictionary of products eligible for promotion (sales < 10).
Challenge
Generate a complete business report.
'''
# Product Inventory Dictionary
#----------------------------------------------------------

products = {
    "P101":{"name":"Laptop","price":55000,"stock":12,"sold":25},
    "P102":{"name":"Mouse","price":500,"stock":20,"sold":40},
    "P103":{"name":"Keyboard","price":1200,"stock":15,"sold":35},
    "P104":{"name":"Monitor","price":10000,"stock":8,"sold":18},
    "P105":{"name":"Printer","price":7000,"stock":5,"sold":12},
    "P106":{"name":"Scanner","price":6500,"stock":3,"sold":8},
    "P107":{"name":"Speaker","price":2500,"stock":10,"sold":22},
    "P108":{"name":"Webcam","price":1800,"stock":6,"sold":14},
    "P109":{"name":"Pendrive","price":700,"stock":30,"sold":50},
    "P110":{"name":"Hard Disk","price":4500,"stock":7,"sold":16},
    "P111":{"name":"SSD","price":6000,"stock":4,"sold":30},
    "P112":{"name":"Router","price":2200,"stock":11,"sold":19},
    "P113":{"name":"Tablet","price":18000,"stock":9,"sold":11},
    "P114":{"name":"Smartphone","price":25000,"stock":13,"sold":28},
    "P115":{"name":"Smartwatch","price":5000,"stock":2,"sold":9},
    "P116":{"name":"Projector","price":30000,"stock":4,"sold":6},
    "P117":{"name":"Camera","price":45000,"stock":5,"sold":10},
    "P118":{"name":"Tripod","price":1500,"stock":12,"sold":17},
    "P119":{"name":"Headphone","price":3000,"stock":8,"sold":27},
    "P120":{"name":"Microphone","price":3500,"stock":6,"sold":15},
    "P121":{"name":"Power Bank","price":1200,"stock":14,"sold":24},
    "P122":{"name":"Charger","price":800,"stock":25,"sold":45},
    "P123":{"name":"Cable","price":300,"stock":40,"sold":60},
    "P124":{"name":"UPS","price":5500,"stock":3,"sold":7},
    "P125":{"name":"Graphics Card","price":35000,"stock":2,"sold":5},
    "P126":{"name":"CPU","price":22000,"stock":6,"sold":13},
    "P127":{"name":"RAM","price":4000,"stock":9,"sold":20},
    "P128":{"name":"Motherboard","price":12000,"stock":5,"sold":8},
    "P129":{"name":"Cooling Fan","price":1000,"stock":7,"sold":12},
    "P130":{"name":"Gaming Chair","price":15000,"stock":4,"sold":4}
}
while True:

    # Menu
    print("\n===== E-COMMERCE INVENTORY & SALES DASHBOARD =====")
    print("1. Display All Products")
    print("2. Add New Product")
    print("3. Update Stock After Sale")
    print("4. Find Out of Stock Products")
    print("5. Products with Stock Less Than 5")
    print("6. Calculate Total Inventory Value")
    print("7. Best Selling Product")
    print("8. Least Selling Product")
    print("9. Total Revenue Generated")
    print("10. Low Stock Report")
    print("11. Products Above Average Sales")
    print("12. Promotion Eligible Products")
    print("13. Complete Business Report")
    print("14. Exit")

    choice = int(input("Enter Choice : "))

# 1. Display all products
#----------------------------------------------------------
    if choice == 1:

        print("\nAll Product Records")

        for pid in products:
            print(pid,
                  products[pid]["name"],
                  products[pid]["price"],
                  products[pid]["stock"],
                  products[pid]["sold"])

# 2. Add Product
#----------------------------------------------------------
    elif choice == 2:

        pid = input("Enter Product ID : ")

        if pid in products:
            print("Product Already Exists")
        else:
            name = input("Enter Product Name : ")
            price = int(input("Enter Price : "))
            stock = int(input("Enter Stock : "))
            sold = int(input("Enter Sold Quantity : "))

            products[pid] = {
                "name": name,
                "price": price,
                "stock": stock,
                "sold": sold
            }

            print("Product Added Successfully")

# 3. Update Stock After Sale
#----------------------------------------------------------
    elif choice == 3:

        pid = input("Enter Product ID : ")

        if pid in products:

            qty = int(input("Enter Quantity Sold : "))

            if qty <= products[pid]["stock"]:

                products[pid]["stock"] -= qty
                products[pid]["sold"] += qty

                print("Stock Updated Successfully")

            else:
                print("Insufficient Stock")

        else:
            print("Product Not Found")

# 4. Out of Stock Products
#----------------------------------------------------------
    elif choice == 4:

        print("\nOut Of Stock Products")

        for pid in products:

            if products[pid]["stock"] == 0:
                print(pid, products[pid]["name"])

# 5. Stock Less Than 5
#----------------------------------------------------------
    elif choice == 5:

        print("\nLow Stock Products")

        for pid in products:

            if products[pid]["stock"] < 5:
                print(pid,
                      products[pid]["name"],
                      products[pid]["stock"])

# 6. Total Inventory Value
#----------------------------------------------------------
    elif choice == 6:

        total_value = 0

        for pid in products:

            value = products[pid]["price"] * products[pid]["stock"]
            total_value += value

        print("Total Inventory Value =", total_value)

 # 7. Best Selling Product
 #-------------------------------------------------------
    elif choice == 7:

        max_sales = -1

        for pid in products:

            if products[pid]["sold"] > max_sales:
                max_sales = products[pid]["sold"]
                best = pid

        print("Best Selling Product")
        print(best,
              products[best]["name"],
              max_sales)

# 8. Least Selling Product
#-------------------------------------------------------
    elif choice == 8:

        min_sales = 999999

        for pid in products:

            if products[pid]["sold"] < min_sales:
                min_sales = products[pid]["sold"]
                least = pid

        print("Least Selling Product")
        print(least,
              products[least]["name"],
              min_sales)

# 9. Total Revenue
#-------------------------------------------------------
    elif choice == 9:

        revenue = 0

        for pid in products:

            revenue += products[pid]["price"] * products[pid]["sold"]

        print("Total Revenue =", revenue)

# 10. Low Stock Report
#-------------------------------------------------------
    elif choice == 10:

        print("\nLOW STOCK REPORT")

        for pid in products:

            if products[pid]["stock"] < 5:
                print(pid,
                      products[pid]["name"],
                      products[pid]["stock"])

 # 11. Products Above Average Sales
#-------------------------------------------------------
    elif choice == 11:

        total_sales = 0

        for pid in products:
            total_sales += products[pid]["sold"]

        average_sales = total_sales / len(products)

        print("Average Sales =", round(average_sales, 2))

        print("\nProducts Above Average Sales")

        for pid in products:

            if products[pid]["sold"] > average_sales:

                print(pid,
                      products[pid]["name"],
                      products[pid]["sold"])

# 12. Promotion Eligible Products
#-------------------------------------------------------
    elif choice == 12:

        promotion = {}

        for pid in products:

            if products[pid]["sold"] < 10:

                promotion[pid] = products[pid]

        print("\nPromotion Eligible Products")

        for pid in promotion:

            print(pid,
                  promotion[pid]["name"],
                  promotion[pid]["sold"])

 # 13. Complete Business Report
#-------------------------------------------------------
    elif choice == 13:

        total_inventory = 0
        total_revenue = 0

        max_sales = -1
        min_sales = 999999

        for pid in products:

            total_inventory += (
                products[pid]["price"] *
                products[pid]["stock"]
            )

            total_revenue += (
                products[pid]["price"] *
                products[pid]["sold"]
            )

            if products[pid]["sold"] > max_sales:
                max_sales = products[pid]["sold"]
                best = pid

            if products[pid]["sold"] < min_sales:
                min_sales = products[pid]["sold"]
                least = pid

        print("\n===== BUSINESS REPORT =====")
        print("Total Products :", len(products))
        print("Inventory Value :", total_inventory)
        print("Revenue :", total_revenue)

        print("\nBest Selling Product :")
        print(best,
              products[best]["name"],
              max_sales)

        print("\nLeast Selling Product :")
        print(least,
              products[least]["name"],
              min_sales)

# 14. Exit
#--------------------------------------------------------
    elif choice == 14:

        print("Program Ended Successfully")
        break

    else:
        print("Invalid Choice")