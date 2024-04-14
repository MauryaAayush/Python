def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10  #here we get the last digit
        reversed_num = reversed_num * 10 + digit 
        num //= 10  #here we get the unit digit
    return reversed_num


num = int(input("Enter a number to reverse: "))

reversed_num = reverse_number(num)
print(f"The reversed number of {num} is {reversed_num}.")
