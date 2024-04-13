# create a program of to reverse a string
# def reverse(string) :


name = input("Enter the string : ")
Rev_name = ""

for char in name :
    Rev_name = char + Rev_name
    
print("Reverse String : ",Rev_name)