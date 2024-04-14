# 34.Write a program to find the perimeter of a rectangle using functions.

def rectangle_perimeter(length, width):
    if length < 0 or width < 0:
        return "Length and width cannot be negative."
    else:
        return 2 * (length + width)


length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

perimeter = rectangle_perimeter(length, width)
print(f"The perimeter of  {length} and width {width} = {perimeter}.")
