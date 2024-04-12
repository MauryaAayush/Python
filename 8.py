# find the factorial 

num = int(input("Enter the Value : "))
factorial = 1


if num < 0 :
    print("The given number is less than 0")
    
elif num == 0 :
    print("The Factorial of " , num , "is 1")
    
else :
    for i in range(1, num + 1) :
        factorial = factorial * i 
    print("The factorial of ",num, "is" ,factorial)
    