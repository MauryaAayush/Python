# program to check string is palindrom or not

name  = input("Enter the string here :")
name = name.lower()

is_palindrome =  True

for i in range(len(name)// 2) :
    if name[i] !=  name[len(name) - i - 1] :
        is_palindrome = False
        break
    

if is_palindrome:
    print("This number is a palindrome.")
    
else :
    print("This number not a palindrome")