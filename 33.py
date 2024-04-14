# 33.Create a program to find the LCM (Least Common Multiple) of two numbers.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = lcm(num1, num2)
print(f"The Least Common Multiple of {num1} and {num2} = {result}.")
