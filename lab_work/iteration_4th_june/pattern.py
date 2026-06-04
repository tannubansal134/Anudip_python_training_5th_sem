# Program to print number pattern and reverse pattern 

# Input number of rows
n = int(input("Enter number of rows: "))

print("\nPattern:")

# Forward pattern
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("\nReverse Pattern:")

# Reverse pattern
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()