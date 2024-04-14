def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)


num = int(input("Enter a number to find the sum of its digits: "))


if num < 0:
    print("Please enter a non-negative number.")
else:
    result = sum_of_digits(num)
    print(f"The sum of digits of {num} is {result}.")
