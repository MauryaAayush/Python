# 20.Create a program to remove duplicates from an array.

num1 = input("Enter the element of the arrey separated by spaces : ")

arrey_elements = num1.split()

dupli_arrey = []

for num in arrey_elements:
    if num.isdigit() and int(num) not in dupli_arrey:
        dupli_arrey.append(int(num))
        
        
print("Arrey after remoiving deplicates : ", dupli_arrey)


# # Input array from the user
# array_input = input("Enter elements of the array separated by spaces: ")

# # Split the input string into a list of substrings
# array_elements = array_input.split()

# # Initialize an empty list to store unique elements
# unique_array = []

# # Iterate over each element in the input array
# for num in array_elements:
#     # Check if the element is a digit and not already in unique_array
#     if num.isdigit() and int(num) not in unique_array:
#         unique_array.append(int(num))

# # Print the array after removing duplicates
# print("Array after removing duplicates:", unique_array)
