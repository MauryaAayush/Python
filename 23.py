def sum_of_natural_numbers(n):
    sum = 0
    count = 1
    while count <= n:
        sum += count
        count += 1
    return sum

num = int(input("Enter a positive integer: "))

if num <= 0:
    print("Please enter a positive integer.")
else:
    result = sum_of_natural_numbers(num)
    print(f"The sum of natural numbers up to {num} is {result}.")
