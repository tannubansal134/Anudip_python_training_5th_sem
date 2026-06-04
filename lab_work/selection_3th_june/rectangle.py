# Program to calculate area and perimeter of a rectangle 

length = float(input("Enter the length: "))
width =  float(input("Enter the width: "))

if length > 0 and width > 0:
    area = length * width
    perimeter = 2 * (length + width)

    print("Area of the rectangle =", area)
    print("Perimeter of the rectangle =", perimeter)
else:
    print("Invalid input! Length and width must be greater than 0.")