num = int(input("Enter the number of the elements in the arrey:  "))
arrey = []

for i in range (num):
    element  = int(input(f"Enter the value { i + 1} : "))
    arrey.append(element)

max_num = max(arrey)

print("Arrey : ", arrey)
print("Largets element from thr arrey is : ",max_num)