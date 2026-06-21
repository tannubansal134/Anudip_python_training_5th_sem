# Write a program to perform division of two numbers entered by the user and handle ZeroDivisionError and ValueError exceptions.

try:
    # Accept two numbers from the user
    #----------------------------------------------------
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = num1 / num2
    print("Result =", result)

# Handle division by zero error
#----------------------------------------------------
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid numeric values.")

else:
    print("Division performed successfully.")

finally:
    print("Program execution completed.")