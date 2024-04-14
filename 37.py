# 37.Create a program to find the reverse of an array using functions.

def reverse_array(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    return arr


input_str = input("Enter space-separated numbers in the array: ")
input_list = input_str.split()
arr = list(map(int, input_list))

reversed_arr = reverse_array(arr)

print("Reversed array:", reversed_arr)
