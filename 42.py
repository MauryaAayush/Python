# Function to print full pyramid pattern

for i in range(1, 6) :
    for k in range(1 , 6) :
        if i == 1 or i == 5 or k == 1 or k == 5 :
            print(k, end = " ")
        else : 
            print("", end = "  ")
    print()