'''Problem Statement
Daily sales figures (in ₹) for 10 days are stored in a list.
Sample Data
sales = [15000, 22000, 18000, 25000, 30000, 17000, 28000, 26000, 21000, 19000]
Tasks
1.
Find the highest sales.
2.
Find the lowest sales.
3.
Calculate average sales.
4.
Count days with sales above ₹20,000.
5.
Display sales figures below average.
Sample Output
Highest Sales: ₹30,000 Lowest Sales: ₹15,000 Average Sales: ₹22,100 Days with Sales Above ₹20,000: 5
Sales Below Average: [15000, 18000, 17000, 21000, 19000]
'''

# List of daily sales figures
#-------------------------------------------------------
sales = [15000, 22000, 18000, 25000, 30000, 17000, 28000, 26000, 21000, 19000]

# Find highest sales
#-------------------------------------------------------
highest_sales = max(sales)

# Find lowest sales
#-------------------------------------------------------
lowest_sales = min(sales)

# Calculate average sales
#-------------------------------------------------------
average_sales = sum(sales) / len(sales)

# Count days with sales above ₹20,000
#-------------------------------------------------------
count_above_20000 = 0
for sale in sales:
    if sale > 20000:
        count_above_20000 += 1

# Create a list of sales below average
#-------------------------------------------------------
below_average = []
for sale in sales:
    if sale < average_sales:
        below_average.append(sale)

# Display results
#-------------------------------------------------------
print("Highest Sales: ₹", highest_sales)
print("Lowest Sales: ₹", lowest_sales)
print("Average Sales: ₹", average_sales)
print("Days with Sales Above ₹20,000:", count_above_20000)
print("Sales Below Average:", below_average)