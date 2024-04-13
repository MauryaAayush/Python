# Function to print full pyramid pattern

A = 65

for i in range(1, 6) :
    A = 65
    for k in range(1 , 6) :
        if i == 1 or i == 5 or k == 1 or k == 5 :
            print(chr(A), end = " ")
        else : 
            print("", end = "  ")
        A+=1
    print()