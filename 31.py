# 31.Create a program to calculate the power of a number using functions.

def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result


base_num = float(input("Enter the base number: "))
exp_num = int(input("Enter the exponent: "))

result = power(base_num, exp_num)
print(f"{base_num} raised to the power of {exp_num} = {result}.")
