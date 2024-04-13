name = input("Enter a string: ")

char_counts = {}

for char in name:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1

print("Character counts : ")
for char, count in char_counts.items():
    print(f"'{char}'-> {count}")
