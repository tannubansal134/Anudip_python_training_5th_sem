# Create a function that checks whether a number is prime using a for loop and returns the result.

def is_prime(num):
    
# Numbers less than 2 are not prime
#------------------------------------------------------
    if num < 2:
        return False

 # Check divisibility from 2 to num-1
 #----------------------------------------------------
    for i in range(2, num):
        if num % i == 0:
            return False    

    return True             


# Accept a number from the user
#-------------------------------------------------------------
number = int(input("Enter a number: "))

# Call the function and display the result
#--------------------------------------------------------------
if is_prime(number):
    print(number, "is a Prime Number")
else:
    print(number, "is not a Prime Number")