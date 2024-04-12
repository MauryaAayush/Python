# swap two variable

a = int(input("Enter the value of A  : "))
b = int(input("Enter the value of B  : "))

a = a + b
b = a - b
a = a - b

print(a)
print(b)