"""
Program: Product Quality Analysis

This program performs the following tasks:
1. Display failed product IDs.
2. Count passed and failed products.
3. Calculate pass percentage.
4. Stop checking if 3 failures are found.
"""

products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

# --------------------------------------------------
# Task 1 & Task 2: Display failed IDs + count pass/fail

pass_count = 0
fail_count = 0
fail_limit = 0

print("Failed Product IDs:")

for product in products:
    pid = product[0]
    status = product[1]

    if status == "Pass":
        pass_count += 1
    else:
        fail_count += 1
        fail_limit += 1
        print(pid)

    # --------------------------------------------------
    # Task 4: Stop if 3 failures are found

    if fail_limit == 3:
        print("\nStopped checking (3 failures found)")
        break

# --------------------------------------------------
# Task 3: Calculate pass percentage

total_checked = pass_count + fail_count

percentage = (pass_count / total_checked) * 100

print("\nPassed Products :", pass_count)
print("Failed Products :", fail_count)
print("Pass Percentage :", percentage)