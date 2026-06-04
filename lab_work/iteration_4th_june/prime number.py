# check the number whether it is a prime or not
num = int(input("Enter a number: "))

count = 0

print("Factors:", end=" ")

for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
        count += 1

print()

if count == 2:
    print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")