num = int(input("Enter the number of the elements in the arrey:  "))
arrey = []

for i in range (num):
    element  = int(input(f"Enter the value { i + 1} : "))
    arrey.append(element)

arrey.sort()

print("Sorted arrey in assending order  : ", arrey)