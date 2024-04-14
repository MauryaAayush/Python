def square_root(n):
    if n < 0:
        return "Square root is not defined for negative numbers."
    elif n == 0:
        return 0
    else:
        return n ** 0.5


num = float(input("Enter a number to find its square root: "))

result = square_root(num)
print(f"The square root of {num} = {result}.")
