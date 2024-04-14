# 39.Create a program to handle file not found exceptions.

try:
    # here we can replace 'filename.txt' with our file name
    with open('39.py', 'r') as file:
        # Perform file operations here (reading, writing, etc.)
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    # Handle the File Not Found exception
    print("Error: File not found.")
except Exception as e:
    # Handle other exceptions
    print("Error:", e)

