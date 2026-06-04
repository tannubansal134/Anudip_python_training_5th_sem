# Read the amount
amount = int(input("Enter amount: "))

# Calculate number of ₹500 notes
notes500 = amount // 500
amount = amount % 500

# Calculate number of ₹200 notes
notes200 = amount // 200
amount = amount % 200

# Calculate number of ₹100 notes
notes100 = amount // 100
amount = amount % 100

# Calculate number of ₹50 notes
notes50 = amount // 50
amount = amount % 50

# Calculate number of ₹20 notes
notes20 = amount // 20
amount = amount % 20

# Calculate number of ₹10 notes
notes10 = amount // 10

# Display only the notes used
if notes500 > 0:
    print("500 x", notes500)

if notes200 > 0:
    print("200 x", notes200)

if notes100 > 0:
    print("100 x", notes100)

if notes50 > 0:
    print("50 x", notes50)

if notes20 > 0:
    print("20 x", notes20)

if notes10 > 0:
    print("10 x", notes10)