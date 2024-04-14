def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def print_primes(start, end):
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)


start_num = int(input("Enter the start number: "))
end_num = int(input("Enter the end number: "))

if start_num >= end_num:
    print("Invalid input. Start number should be less than end number.")
else:
    print_primes(start_num, end_num)
