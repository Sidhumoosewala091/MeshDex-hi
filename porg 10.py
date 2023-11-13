import math

def calculate_rectangle_area(length, width):
    return length * width

def calculate_square_area(side):
    return side * side

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def menu_driven_area_calculation():
    while True:
        print("\nMenu:")
        print("1. Calculate area of a rectangle")
        print("2. Calculate area of a square")
        print("3. Calculate area of a circle")
        print("4. Calculate area of a triangle")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            length = float(input("Enter length of rectangle: "))
            width = float(input("Enter width of rectangle: "))
            print(f"Area of rectangle: {calculate_rectangle_area(length, width)}")
        elif choice == 2:
            side = float(input("Enter side length of square: "))
            print(f"Area of square: {calculate_square_area(side)}")
        elif choice == 3:
            radius = float(input("Enter radius of circle: "))
            print(f"Area of circle: {calculate_circle_area(radius)}")
        elif choice == 4:
            base = float(input("Enter base length of triangle: "))
            height = float(input("Enter height of triangle: "))
            print(f"Area of triangle: {calculate_triangle_area(base, height)}")
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

# Example usage
menu_driven_area_calculation()
