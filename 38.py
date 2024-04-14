# 38.Write a program to handle division by zero exception.

def reverse_array(arr):
    n = len(arr)
    reversed_arr = []
    for i in range(n - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

# Input from the user
input_str = input("Enter space for separate numbers in the array: ")
input_list = input_str.split()
arr = list(map(int, input_list))

reversed_arr = reverse_array(arr)
print("Original array:", arr)
print("Reversed array:", reversed_arr)
