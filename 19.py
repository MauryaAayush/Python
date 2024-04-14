# 19.Write a program to find the intersection of two arrays.

num1 = input("Enter elements of array1 separated by spaces: ")
num2 = input("Enter elements of array2 separated by spaces: ")

# Convert user input strings into arrays for array1
array1 = []
for num in num1.split():
    if num.isdigit():
        array1.append(int(num))

# Convert user input strings into arrays for array2
array2 = []
for num in num2.split():
    if num.isdigit():
        array2.append(int(num))

intersection = list(set(array1) & set(array2))

if intersection:
    print("Intersection of array1 and array2:", intersection)
else:
    print("There is no intersection between the arrays.")
