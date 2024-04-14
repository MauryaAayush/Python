def factorial(n) :
    if n == 0:
        return 1
    else :
        return n * factorial(n - 1)
    
    
num = int(input("Enter the value : "))
    
if num < 0 :
    print("factorial of this number doesn't exixt")
        
else : 
    result = factorial(num)
    print(f"The factorial of {num} is {result}.")