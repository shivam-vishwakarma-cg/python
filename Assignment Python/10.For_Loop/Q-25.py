text = input("Enter a string: ")
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
uppercase_count = 0

for char in text:
    if char in uppercase_letters:
        uppercase_count += 1

print("Uppercase characters count:", uppercase_count)