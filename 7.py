# to check given year is a leap year

Year = int(input("Enter the Year : "))

if Year < 0 :
    
    print ("Enter the Year more than 1")
    
else :     
    if Year % 4 == 0 :
        print ("This is a leap year")
    else : 
        print("This Year is not a leap year")