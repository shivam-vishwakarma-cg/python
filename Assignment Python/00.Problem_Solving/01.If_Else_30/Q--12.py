char = input("Enter one character:")
if char.isupper():
    print("Uppercase alphabet")
elif char.islower():
    print("Lowercase alphabet")
elif char.isdigit():
    print("Digit")
else:
    print("Special character")