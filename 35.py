# 35.Create a program to implement bubble sort using functions.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = list(map(int, input("Enter numbers to sort and also  use space for separation: ").split()))

print("Original array:", arr)

bubble_sort(arr)

print("Sorted array:", arr)
