# Function to print full pyramid pattern

for i in range(0, 6) :
    for k in range(0 , 6) :
        if i == 0 or i == 5 or k == 0 or k == 5 :
            print("*", end = " ")
        else : 
            print("", end = "  ")
    print()