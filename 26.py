def is_armstrong(num):
    
    num_str = str(num)
    num_digits = len(num_str)

   
    total = sum(int(digit) ** num_digits for digit in num_str)

   
    return total == num



num = int(input("Enter a value : "))

if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
