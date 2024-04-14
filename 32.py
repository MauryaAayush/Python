# 32.Write a program to find the area of a circle using functions.


import math

def circle_area(radius):
    if radius < 0:
        return "Radius cannot be negative."
    else:
        return math.pi * radius ** 2

# Input from the user
radius = float(input("Enter the radius of the circle: "))

area = circle_area(radius)
print(f"The area of the circle with radius {radius} is {area}.")
