#gievn a transaction list of an atm an perform the following
transactions=[5000, -2000, 3000, -1000, -500, 7000]
#to calculate current balance
balance = 0
for t in transactions:
      balance+=t

print("Current Balance:", balance)

#Count deposits and withdrawls
deposit_count = 0
withdrawal_count = 0

for t in transactions:
    if t > 0:
        deposit_count += 1
    else:
        withdrawal_count += 1

print("Total Deposits:", deposit_count)
print("Total Withdrawals:", withdrawal_count)

#Largest Deposit and Largest Withdrawl
largest_deposit = transactions[0]
largest_withdrawal = transactions[1]

for t in transactions:
    if t > 0 and t > largest_deposit:
        largest_deposit = t

    if t < 0 and t < largest_withdrawal:
        largest_withdrawal = t

print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)

# 4. Create separate lists
deposits = []
withdrawals = []

for t in transactions:
    if t > 0:
        deposits.append(t)
    else:
        withdrawals.append(t)

print("Deposits List:", deposits)
print("Withdrawals List:", withdrawals)