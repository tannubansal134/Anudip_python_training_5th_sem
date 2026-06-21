# Accept 10 integers from the user and separate them into two different lists containing even and odd numbers using a for loop.

# Create empty lists for even and odd numbers
#----------------------------------------------------------
even_numbers = []
odd_numbers = []

# Accept 10 integers from the user
#------------------------------------------------
for i in range(10):
    num = int(input("Enter an integer: "))

 # Check whether the number is even or odd
 #------------------------------------------------

    if num % 2 == 0:
        even_numbers.append(num)  
    else:
        odd_numbers.append(num)   

# Display the lists
#--------------------------------------------------
print("\nEven Numbers List:", even_numbers)
print("Odd Numbers List:", odd_numbers)