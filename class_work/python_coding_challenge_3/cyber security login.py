'''A file named login_logs.txt contains user login attempts in the following format: 
username,status anuj,Success rahul,Failed anuj,Failed priya,Failed rahul,Failed neha,Success anuj,Failed karan,Failed rahul,Success priya,Failed 
Tasks 
1.	Count successful and failed login attempts.  
2.	Identify users with more than 2 failed attempts.  
3.	Create a dictionary storing the number of failures per user.  
4.	Create a set of users who logged in successfully.  
5.	Display users whose accounts should be reviewed.  
'''
# Read login logs from file

success_count = 0
failed_count = 0

failure_dict = {}
successful_users = set()

with open("login_logs.txt", "r") as file:
    for line in file:
        line = line.strip()

        if not line:
            continue

        username, status = line.split(",")

        if status.lower() == "success":
            success_count += 1
            successful_users.add(username)

        elif status.lower() == "failed":
            failed_count += 1

            if username in failure_dict:
                failure_dict[username] += 1
            else:
                failure_dict[username] = 1

# Users with more than 2 failed attempts
review_accounts = []

for user, count in failure_dict.items():
    if count > 2:
        review_accounts.append(user)

# Output
print("Successful Login Attempts:", success_count)
print("Failed Login Attempts:", failed_count)

print("\nFailure Count per User:")
for user, count in failure_dict.items():
    print(user, ":", count)

print("\nUsers with Successful Logins:")
print(successful_users)

print("\nAccounts Requiring Review:")
if review_accounts:
    print(review_accounts)
else:
    print("None")

