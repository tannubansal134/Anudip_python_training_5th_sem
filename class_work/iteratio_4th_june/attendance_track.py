present = 0
absent = 0

n = int(input("Enter total number of students: "))

i = 1

while i <= n:
    status = input("Student(P/A)"": ".format(i))

    if status == 'p':
        present += 1
    elif status == 'a':
        absent += 1
    else:
        print("Invalid input")
        continue

    i += 1

print("\nTotal Present Students:", present)
print("Total Absent Students:", absent)