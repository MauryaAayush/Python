# 36.Write a program to calculate the average of elements in an array using functions.

def calculate_average(arr):
    if len(arr) == 0:
        return "Array is empty. Cannot calculate average."
    else:
        total = sum(arr)
        average = total / len(arr)
        return average


input_str = input("Enter space-separated numbers in the array: ")
input_list = input_str.split()
arr = list(map(float, input_list))

average = calculate_average(arr)
if isinstance(average, str):  # Check if average is a string 
    print(average)
else:
    print("Array:", arr)
    print("Average:", average)
