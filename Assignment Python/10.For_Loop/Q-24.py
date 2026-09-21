text = input("Enter a string: ")
count_a = 0

for char in text:
    if char == "a":
        count_a += 1

print("Count of 'a':", count_a)