# 40.Write a program to handle index out-of-range exceptions.

try:
   
    my_list = [1, 2, 3]

   
    index = 2  # change this index to see the result 
    value = my_list[index]
    print("Value at index", index, ":", value)
except IndexError:
    print("Error: Index out of range.")
except Exception as e:
    print("Error:", e)
