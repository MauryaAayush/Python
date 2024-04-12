# check the number is prime or not 

num = int(input("Enter the value : "))

if num > 1 :

    for i in range(2 , (num // 2) + 1) :
        
        if num % i :
            print("This is prime number")
            break
        else :
            print("This is a not prime")
            break
else : 
     print("Enter more than 1 number")



    
  
  
  
  
  # if num % 2 != 0 & num % 3 != 0 & num % 5 != 0 & num % 7 != 0 :
    #     print("This number is a not a prime number")
    # else :
    #     print("This number is a prime number")    