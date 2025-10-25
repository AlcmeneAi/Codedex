print("Area Calculator")
print("-"*30)

print("User Instructions:")

print("1. Enter the shape you want to calculate the area for (rectangle, circle, triangle).")
print("2. Enter the dimensions required for the shape.")
print("-"*30)

shape = input("Enter the shape (rectangle, circle, triangle): ").lower()

if shape == "rectangle":
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))
    area = width * height
elif shape == "circle":
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14159 * radius**2
elif shape == "triangle":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
else:
    area = 0

print(f"The area of the {shape} is: {area}")