"""
Program: 2D Figure Calculator

This program allows the user to:
1. Select a 2D figure.
2. Enter the required dimensions.
3. Calculate Area or Perimeter.
4. Repeat operations for the selected figure.
5. Return to the main menu or Exit.

Figures Available:
1. Circle
2. Rectangle
3. Square
"""

import math

# ---------------------------------------------------------
# Function to calculate area of a circle

def circle_area(radius):
    return math.pi * radius * radius


# ---------------------------------------------------------
# Function to calculate perimeter of a circle

def circle_perimeter(radius):
    return 2 * math.pi * radius


# ---------------------------------------------------------
# Function to calculate area of a rectangle

def rectangle_area(length, breadth):
    return length * breadth


# ---------------------------------------------------------
# Function to calculate perimeter of a rectangle

def rectangle_perimeter(length, breadth):
    return 2 * (length + breadth)


# ---------------------------------------------------------
# Function to calculate area of a square

def square_area(side):
    return side * side


# ---------------------------------------------------------
# Function to calculate perimeter of a square

def square_perimeter(side):
    return 4 * side

# ---------------------------------------------------------
# Main Program Loop
# Displays figure menu repeatedly until user exits

while True:

    print("\n========== 2D FIGURE CALCULATOR ==========")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Exit")

    figure = int(input("Enter your choice: "))

    # -----------------------------------------------------
    # Exit Option
   
    if figure == 4:
        print("Thank You for using the program.")
        break

    # -----------------------------------------------------
    # Circle Section
    
    elif figure == 1:

        radius = float(input("Enter Radius: "))

        while True:
            print("\n--- Circle Operations ---")
            print("1. Area")
            print("2. Perimeter")
            print("3. Exit from Circle")

            choice = int(input("Enter Operation: "))

            if choice == 1:
                print("Area =", circle_area(radius))

            elif choice == 2:
                print("Perimeter =", circle_perimeter(radius))

            elif choice == 3:
                break

            else:
                print("Invalid Choice")

    # -----------------------------------------------------
    # Rectangle Section
    
    elif figure == 2:

        length = float(input("Enter Length: "))
        breadth = float(input("Enter Breadth: "))

        while True:
            print("\n--- Rectangle Operations ---")
            print("1. Area")
            print("2. Perimeter")
            print("3. Exit from Rectangle")

            choice = int(input("Enter Operation: "))

            if choice == 1:
                print("Area =", rectangle_area(length, breadth))

            elif choice == 2:
                print("Perimeter =", rectangle_perimeter(length, breadth))

            elif choice == 3:
                break

            else:
                print("Invalid Choice")

    # -----------------------------------------------------
    # Square Section
   
    elif figure == 3:

        side = float(input("Enter Side: "))

        while True:
            print("\n--- Square Operations ---")
            print("1. Area")
            print("2. Perimeter")
            print("3. Exit from Square")

            choice = int(input("Enter Operation: "))

            if choice == 1:
                print("Area =", square_area(side))

            elif choice == 2:
                print("Perimeter =", square_perimeter(side))

            elif choice == 3:
                break

            else:
                print("Invalid Choice")

    