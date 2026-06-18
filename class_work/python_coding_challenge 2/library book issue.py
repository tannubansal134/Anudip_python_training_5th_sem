'''Problem Statement
A library stores the number of times books were issued during a month.
Sample Data
book_issues = [15, 8, 22, 10, 18, 5, 30, 12, 20, 25]
Tasks
1.Find the maximum number of issues.
2.Find the minimum number of issues.
3.Calculate the average number of issues.
4.Count books issued more than 15 times.
5.Create a list of books issued fewer than 10 times.
'''

# Sample data
#-------------------------------------------------------
book_issues = [15, 8, 22, 10, 18, 5, 30, 12, 20, 25]

# Find maximum number of issues
#-------------------------------------------------------
max_issues = max(book_issues)

# Find minimum number of issues
#-------------------------------------------------------
min_issues = min(book_issues)

# Calculate average number of issues
#-------------------------------------------------------
average_issues = sum(book_issues) / len(book_issues)

# Count books issued more than 15 times
#-------------------------------------------------------
count_more_than_15 = 0
for issue in book_issues:
    if issue > 15:
        count_more_than_15 += 1

# Create a list of books issued fewer than 10 times
#-------------------------------------------------------
less_than_10 = []
for issue in book_issues:
    if issue < 10:
        less_than_10.append(issue)

# Display results
#---------------------------------------------------------
print("Maximum Issues:", max_issues)
print("Minimum Issues:", min_issues)
print("Average Issues:", average_issues)
print("Books Issued More Than 15 Times:", count_more_than_15)
print("Books Issued Fewer Than 10 Times:", less_than_10)