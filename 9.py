# write a program to generate fibonacii series
len = int(input("Enter the length of series = "))

start = 0
last = 1
next_number = last
count = 1

print("0  1 ", end= " ")

while count <= len :
        print(next_number, end = "  ")
        count += 1
        
        start = last
        last = next_number
        
        next_number = start + last
# print(" achha")